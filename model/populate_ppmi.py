import numpy as np
import pandas as pd
import os, math
from time import sleep
from tqdm import tqdm

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

#read in output csv file from reorganize file
df_co_occ = pd.read_csv('../reorganized_data/cluster1/filled_matrix.csv', index_col='word_set')
print("filled coocurence matrix",df_co_occ.shape)
print(df_co_occ.head())
print("===================")
#df_co_occ = df_co_occ.loc[:, ~df_co_occ.columns.str.contains('^Unnamed')]
#df_co_occ = df_co_occ.set_index('word')
df_vocab_dict = pd.read_csv('../reorganized_data/cluster1/vocab_dict.csv')
df_vocab_dict = df_vocab_dict.set_index("Unnamed: 0")
print("vocab dict")
print(df_vocab_dict.head())
print("===============")
sumofcounts = df_vocab_dict["count"].sum()

emptymatrix = df_co_occ.copy()
emptymatrix_columns = emptymatrix.columns.tolist()
#print("emptyatrix columns",emptymatrix_columns)
emptymatrix_rows = emptymatrix.index.tolist()
#emptymatrix = emptymatrix.loc[:, ~emptymatrix.columns.str.contains('^Unnamed')]
#emptymatrix = emptymatrix.set_index('word') # Changing index from nums to words

for col in emptymatrix.columns:
    emptymatrix[col].values[:] = 0

#print(emptymatrix)
#print(emptymatrix.shape)
#emptymatrix = emptymatrix.reset_index().dropna().set_index('word') # changing index from nums to words

allwords = emptymatrix_columns
allwordslen = len(allwords)
matrix_words = emptymatrix.columns.tolist()
#vocab_list = df_vocab_dict["Unnamed: 0"].tolist()
for a in emptymatrix_columns:
    for b in emptymatrix_rows:
        coval = df_co_occ.loc[a,b]
        try:
          acount = df_vocab_dict.loc[a,"count"]
        except KeyError:
          acount = 0
        try:
          bcount = df_vocab_dict.loc[b,"count"]
        except KeyError:
          bcount = 0
        numer = coval * sumofcounts
        denom = acount * bcount
        pmival = np.log(numer / denom)
        if (pmival < 0 or math.isnan(pmival)):
            pmival = 0
        emptymatrix.at[a,b] = pmival
        #print("ppmi value",emptymatrix.at[a,b])
print(emptymatrix)
print(emptymatrix.shape)
emptymatrix.to_csv('../reorganized_data/cluster1/ppmi_matrix.csv')
