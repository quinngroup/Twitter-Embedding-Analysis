import numpy as np
import pandas as pd
import os

df = pd.read_csv('../../reorganized_data/cluster1/output.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df[:5])

alltweets = []
allwords = []
window = 5
vocab_dictionary = {}

for index, row in df.iterrows():
        alltweets.append(row["preprocessed_text"])

for tweet in alltweets:
        tweet = tweet.replace(']','').replace('[','')
        tweet = tweet.replace('"','').split(",")
        for word in tweet:
                if word not in allwords:
                    allwords.append(word)
                    vocab_dictionary[word] = 1
                else:
                    vocab_dictionary[word] += 1

print(vocab_dictionary)

dict_df = pd.DataFrame.from_dict(vocab_dictionary, orient='index', columns=['count'])

print(dict_df)

dict_df.to_csv('../../reorganized_data/cluster1/vocab_dict.csv')
print(len(vocab_dictionary) == len(allwords))
print('Completed')
