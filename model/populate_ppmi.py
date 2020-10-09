import numpy as np
import pandas as pd
import os

#read in output csv file from reorganize file
df_co_occ = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
df_co_occ = df_co_occ.loc[:, ~df_co_occ.columns.str.contains('^Unnamed')]
df_co_occ = df_co_occ.set_index('word')
df_vocab_dict = pd.read_csv('../../reorganized_data/cluster1/vocab_dict.csv')

emptymatrix = pd.read_csv('../../reorganized_data/cluster1/empty_matrix.csv')
emptymatrix = emptymatrix.loc[:, ~emptymatrix.columns.str.contains('^Unnamed')]
emptymatrix = emptymatrix.set_index('word') # Changing index from nums to words
emptymatrix = emptymatrix.reset_index().dropna().set_index('word') # changing index from nums to words

allwords = df_vocab_dict.iloc[:,0]
allwordslen = len(allwords)

for w in allwords:
    for c in allwords:
        coval = df_co_occ.loc[w,c]
        wcount = df_vocab_dict.loc[w]
        ccount = df_vocab_dict.loc[c]
        numer = coval * allwordslen
        denom = wcount * ccount
        pmival = np.log(numer / denom)
        if (pmival < 0):
            pmival = 0
        emptymatrix[w,c] = pmival
        print(pmival)

emptymatrix.to_csv('../../reorganized_data/cluster1/ppmi_matrix.csv')
