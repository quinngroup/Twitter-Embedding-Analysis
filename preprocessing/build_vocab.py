import pandas as pd
import nltk
nltk.download('stopwords')
from tqdm import tqdm

# read in vocab files
clust_vocab = pd.read_csv("../reorganized_data/cluster0/vocab_dict.csv")
clust_vocab = clust_vocab.rename(columns={"Unnamed: 0": "word_set"})
print(clust_vocab[:5])

clust_vocab = clust_vocab.sort_values(by=['count'], ascending=False).reset_index(drop=True).dropna()
print(clust_vocab[:5])
print(len(clust_vocab))

def build_with_x(freq=200):
  '''
  build vocabulary from words
  that occur more than freq times
  '''
  clust_vocab = pd.read_csv("../reorganized_data/cluster1/vocab_dict.csv")
  print("cluster vocab")
  print(clust_vocab[:5])
  all_vocab = clust_vocab.copy()
  print(all_vocab[:5])
  for index, row in tqdm(clust_vocab.iterrows()):
    if row["count"] < freq:
      all_vocab = all_vocab.drop([index])

  all_vocab = all_voab.dropna()
  return all_vocab

def build_with_min(clust_vocab, l=10000):
  # create list
  print("origin length clust_vocab", len(clust_vocab))
  all_vocab = pd.DataFrame(clust_vocab[:l]) # create initial vocab from most common words from first cluster
  all_vocab = all_vocab.rename(columns={"Unnamed: 0": "word_set"})
  print(all_vocab[:5], len(all_vocab))
  min = all_vocab.iloc[-1] # find first minimum
  #print("first min",min)

  for i in range(1,18):
    print("cluster",i)
    clust_vocab = pd.read_csv("../reorganized_data/cluster"+str(i)+"/vocab_dict.csv").dropna()
    clust_vocab = clust_vocab.rename(columns={"Unnamed: 0": "word_set"})
    #print(clust_vocab[:5])

    #print(len(clust_vocab))
    # iterate through vocab
    for index, row in clust_vocab.iterrows():
      if min["count"] < row["count"]:
        all_vocab.iloc[-1] = row
        all_vocab = all_vocab.sort_values(by=["count"], ascending=False).reset_index(drop=True)
        min = all_vocab.iloc[-1]
        #print(len(all_vocab))
        #print("new min", min["word_set"], min["count"])
    #d = {'count':'sum'}
    #all_vocab = all_vocab.groupby(by='word_set', sort=False, as_index=False).agg(d).reindex(columns=all_vocab.columns)
  all_vocab = all_vocab.dropna()
  return all_vocab

vocab = build_with_min(clust_vocab)
print(len(vocab))
d = {'count':'sum'}
vocab = vocab.groupby(by='word_set', sort=False, as_index=False).agg(d).reindex(columns=vocab.columns)
vocab.to_csv("global_vocab.csv")
print(vocab[:15])
print(len(vocab))
