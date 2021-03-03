import numpy as np
import pandas as pd
import os, re

# df = pd.read_csv('../../reorganized_data/cluster1/output0.csv')
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
# print("read file")

alltweets = []
allwords = {}
window = 5

for i in range(0,12):
  df = pd.read_csv('../../reorganized_data/cluster1/output'+str(i)+'.csv')
  df = df.loc[:, ~df.columns.str.contains('^Unamed')]
  print("read output", i)


  for index, row in df.iterrows():
    tweet = row["preprocessed_text"]
    # print(tweet)
    tweet = re.sub(r'[^\w\s]','',tweet)
    tweet = re.sub(r'[^a-zA-Z]+',' ',tweet).split(" ")
    # print(tweet)
    for word in tweet:
      allwords[word] = 0
  print("finished preprocessing and splitting output",i)

numberofwords = len(allwords)
print("vocab size:",numberofwords)

dictionary = pd.DataFrame(columns=["word"],low_memory=False, dtype={"word":"string"})

words_list = list(allwords.keys())
for word in words_list:
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
print("finished")
