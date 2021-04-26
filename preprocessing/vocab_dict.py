import numpy as np
import pandas as pd
import os, re
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
vocab_dictionary = {}

for clust_num in range(11,18):
  for i in range(0, 12):
    print("cluster "+str(clust_num)+", output "+str(i))
    path = '../reorganized_data/cluster'+str(clust_num)+'/output'+str(i)+'.csv'
    df = pd.read_csv(open(path))

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    print(len(df))

    alltweets = []
    allwords = []
    window = 5

    for index, row in df.iterrows():
      alltweets.append(row["preprocessed_text"])

    for tweet in alltweets:
      tweet = re.sub(r'[^\w\s]','',str(tweet))
      tweet = re.sub(r'[^a-zA-Z]+',' ',tweet).split(" ")
      for word in tweet:
        if word not in allwords:
          if word not in stop_words:
            allwords.append(word)
            vocab_dictionary[word] = 1
        else:
            vocab_dictionary[word] += 1

  print(vocab_dictionary)

  dict_df = pd.DataFrame.from_dict(vocab_dictionary, orient='index', columns=['count'])

  print(dict_df)

  dict_df.to_csv('../reorganized_data/cluster'+str(clust_num)+'/vocab_dict.csv')
  print("saved cluster "+str(clust_num)+" vocab")
  print(len(vocab_dictionary) == len(allwords))
print('Completed')
