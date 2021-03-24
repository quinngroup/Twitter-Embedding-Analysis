import pandas as pd
from tqdm import tqdm

# read in vocab files
clust_vocab = pd.read_csv("../../reorganized_data/cluster0/vocab_dict.csv")
clust_vocab = clust_vocab.rename(columns={"Unnamed: 0": "word"})
print(clust_vocab[:5])

clust_vocab = clust_vocab.sort_values(by=['count'], ascending=False).reset_index(drop=True).dropna()
print(clust_vocab[:5])
print(len(clust_vocab))

def build_with_x(freq=200):
  '''
  build vocabulary from words
  that occur more than freq times
  '''
  clust_vocab = pd.read_csv("../../reorganized_data/cluster1/vocab_dict.csv")
  print("cluster vocab")
  print(clust_vocab[:5])
  all_vocab = clust_vocab.copy()
  print(all_vocab[:5])
  for index, row in tqdm(clust_vocab.iterrows()):
    if row["count"] < freq:
      all_vocab = all_vocab.drop([index])

  all_vocab = all_voab.dropna()
  return all_vocab
      

def build_with_min():
  # create list
  all_vocab = pd.DataFrame(clust_vocab[:10000]) # create initial vocab from most common words from first cluster
  print(all_vocab[:10])
  min = all_vocab.iloc[-1] # find first minimum
  print("first min",min)

  clust_vocab = pd.read_csv("../../reorganized_data/cluster1/vocab_dict.csv").dropna()
  print(clust_vocab[:5])

  print(len(clust_vocab))
  # iterate through vocab
  for index, row in tqdm(clust_vocab.iterrows()):
    if min["count"] < row["count"]:
      all_vocab.iloc[-1] = row
      all_vocab = all_vocab.sort_values(by=["count"], ascending=False).reset_index(drop=True)
      min = all_vocab.iloc[-1]
      print(len(all_vocab))
      # print("new min", min["word"], min["count"])

  all_vocab = all_vocab.dropna()
  return all_vocab

vocab = build_with_x()
print(vocab[:15])
print(len(vocab))
