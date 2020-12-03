import numpy as np
import pandas as pd
import os
from time import sleep
from tqdm import tqdm

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

#read in output csv file from reorganize file
df_co_occ = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
df_co_occ = df_co_occ.loc[:, ~df_co_occ.columns.str.contains('^Unnamed')]
df_co_occ = df_co_occ.set_index('word')
df_vocab_dict = pd.read_csv('../../reorganized_data/cluster1/vocab_dict.csv')
df_vocab_dict = df_vocab_dict.set_index("Unnamed: 0")
print(df_vocab_dict)
sumofcounts = df_vocab_dict["count"].sum()

emptymatrix = df_co_occ.copy()
emptymatrix_columns = emptymatrix.columns.tolist()
emptymatrix_rows = emptymatrix.index.tolist()
#emptymatrix = emptymatrix.loc[:, ~emptymatrix.columns.str.contains('^Unnamed')]
#emptymatrix = emptymatrix.set_index('word') # Changing index from nums to words

for col in emptymatrix.columns:
    emptymatrix[col].values[:] = 0

print(emptymatrix)
print(emptymatrix.shape)
#emptymatrix = emptymatrix.reset_index().dropna().set_index('word') # changing index from nums to words

allwords = df_vocab_dict.iloc[:,0].tolist()
allwordslen = len(allwords)
matrix_words = emptymatrix.columns.tolist()
#vocab_list = df_vocab_dict["Unnamed: 0"].tolist()
for a in tqdm(emptymatrix_columns):    
    for b in emptymatrix_rows:
        coval = df_co_occ.loc[a,b]
        acount = df_vocab_dict.loc[a,"count"]
        bcount = df_vocab_dict.loc[b,"count"]
        numer = coval * sumofcounts
        denom = acount * bcount
        pmival = np.log(numer / denom)
        if (pmival < 0):
            pmival = 0
        emptymatrix.at[b,a] = pmival
        # if (coval > 0):
        #     print("a:",a)
        #     print("b:",b)
        #     print("coval:",coval)
        #     print("acount:",acount)
        #     print("bcount:",bcount)
        #     print("pmival:",pmival)

# print(Diff(allwords, matrix_words))
# print(len(allwords))
# print(type(allwords))
# print(len(matrix_words))
# print(type(matrix_words))
# print(len(vocab_list))
# print(type(vocab_list))
# print(Diff(vocab_list, matrix_words))
# print("df_vocab_dict:", df_vocab_dict)
# print("df_vocab_dict len:", len(df_vocab_dict))
#for w in allwords:
#    for c in allwords:
#         coval = df_co_occ.loc[w,c]
#         wcount = df_vocab_dict.loc[w]
#         ccount = df_vocab_dict.loc[c]
#         numer = coval * allwordslen
#         denom = wcount * ccount
#         pmival = np.log(numer / denom)
#         if (pmival < 0):
#             pmival = 0
#         emptymatrix[w,c] = pmival
#         print(pmival)
print(emptymatrix)
print(emptymatrix.shape)
emptymatrix.to_csv('../../reorganized_data/cluster1/ppmi_matrix11.csv')
