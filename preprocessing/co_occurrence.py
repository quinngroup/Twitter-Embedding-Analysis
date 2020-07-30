import numpy as np
import pandas as pd
import os

df = pd.read_csv('../../reorganized_data/cluster1/output.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

alltweets = []
allwords = []
window = 5
co_occ_dictionary = {}

for index, row in df.iterrows():
        alltweets.append(row["preprocessed_text"])

for tweet in alltweets:
        tweet = tweet.replace(']','').replace('[','')
        tweet = tweet.replace('"','').split(",")
        for word in tweet:
                if word not in allwords:
                        allwords.append(word)

numberofwords = len(allwords)

dictionary = pd.DataFrame(columns=["word"])

for word in allwords:
        new_row = {"word":word}
        dictionary = dictionary.append(new_row, ignore_index=True)

dictionary = dictionary.sort_values(by=['word'])

dictionary = dictionary.set_index('word')

for word in allwords:
        dictionary[word] = 0

dictionary = dictionary.sort_index(axis=1)

print(dictionary)
print(":^)")

dictionary.to_csv("../../reorganized_data/cluster1/empty_matrix.csv")
