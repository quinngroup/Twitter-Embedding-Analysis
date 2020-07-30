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
	for word in tweet:
		if word not in allwords:
			allwords.append(word)

numberofwords = len(allwords)

dictionary = pd.DataFrame(columns=["word"])

for word in allwords:
	new_row = {"word":word}
	dictionary = dictionary.append(new_row, ignore_index=True)

dictionary = dictionary.set_index('word')

dictionary = dicionary.sort_index(key=lambda x: x.str.lower())

for word in allwords:
	dictionary[wor] = 0

dictionary = dictionary.sort_index(inplace=True, axis=1)

print(dictionary)
