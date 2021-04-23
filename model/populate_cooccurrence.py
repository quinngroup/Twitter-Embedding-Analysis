import numpy as np
import pandas as pd
import os, re
from tqdm import tqdm

#~~~~ Look into reducing code by stripping index from empty and using it as vocabualry ~~~~
allwords = pd.read_csv('empty_matrix.csv')
allwords = allwords["word_set"].tolist() # gets vocabulary from word_set
print("read allwords")

emptymatrix = pd.read_csv('empty_matrix.csv', index_col='word_set')
print("read empty matrix")

for i in range(12):
  df = pd.read_csv('../reorganized_data/cluster3/output'+str(i)+'.csv')
  alltweets = df["preprocessed_text"].tolist()
  print("read alltweets")

  print("window counts starting now")
  for word in allwords:
    for separateddocument in alltweets:
      # These two lines below change the `separateddocument` from str to list
      separateddocument = str(separateddocument)
      separateddocument = separateddocument.replace(']','').replace('[','')
      separateddocument = separateddocument.replace('\'','').replace('"',"")
      separateddocument = re.sub(r'[^\w\s]','',str(separateddocument))
      separateddocument = re.sub(r'[^a-zA-Z+]',' ',separateddocument)
      separateddocument = re.sub(' +',' ',separateddocument).split(" ")
      #print(word,"---" ,separateddocument)
      if word in separateddocument:
        #print("word is found in doc")
        indices = [i for i, x in enumerate(separateddocument) if x == word]
        for index in indices:
          sliced_front = separateddocument[index-5 if index-5 > 0 else 0: index]
          sliced_end = separateddocument[index+1: index+6]
          wordsrange = sliced_front + sliced_end
          for windowword in wordsrange:
            if windowword in allwords:
              emptymatrix.at[word, windowword] += 1

emptymatrix.to_csv('../reorganized_data/cluster3/filled_matrix.csv')
