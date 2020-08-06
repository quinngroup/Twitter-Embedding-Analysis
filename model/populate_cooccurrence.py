import numpy as np
import pandas as pd
import os

#read in output csv file from reorganize file
df = pd.read_csv('../../reorganized_data/cluster1/output.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

#initialize variables
alltweets = []
allwords = []
window = 5

#get all tweets in one array
for index, row in df.iterrows():
    alltweets.append(row["preprocessed_text"])

#get all unique words in the tweets in one array (vocabulary)    
for tweet in alltweets:
    # These two lines before change the `tweet` from str to list
    tweet = tweet.replace(']','').replace('[','')
    tweet = tweet.replace('"','').split(",")
    for word in tweet:
        if word not in allwords:
            (allwords.append(word))

#determine N (the length of the vocabulary)
#print('number of all words: ' + str(len(allwords)))

emptymatrix = pd.read_csv('../../reorganized_data/cluster1/empty_matrix.csv')
emptymatrix = emptymatrix.loc[:, ~emptymatrix.columns.str.contains('^Unnamed')]
emptymatrix = emptymatrix.set_index('word') # Changing index from nums to words
emptymatrix = emptymatrix.reset_index().dropna().set_index('word') # changing index from nums to words

pd.set_option('display.max_rows', 9000)
pd.set_option('display.max_columns', 9000)

for word in allwords:
    for separateddocument in alltweets:
        # These two lines below change the `separateddocument` from str to list
        separateddocument = separateddocument.replace(']','').replace('[','')
        separateddocument = separateddocument.replace('"','').split(",")
        if word in separateddocument:
            indices = [i for i, x in enumerate(separateddocument) if x == word]
            for index in indices:
                sliced_front = separateddocument[index-5 if index-5 > 0 else 0: index]
                sliced_end = separateddocument[index+1: index+6]
                wordsrange = sliced_front + sliced_end
                for windowword in wordsrange:
                    emptymatrix.at[word, windowword] += 1

emptymatrix.to_csv('../../reorganized_data/cluster1/filled_matrix.csv')
