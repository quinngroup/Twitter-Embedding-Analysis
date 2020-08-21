import scipy
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs
import pandas as pd
import numpy as np

filled = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
filled = filled.loc[:, ~filled.columns.str.contains('^Unnamed')]
listofwords = filled['word'][0:6000].to_list()
print(listofwords)

print('created list')
filled = filled.set_index('word')
filled = filled.reset_index().dropna().set_index('word')

sparsematrix = filled.to_numpy()
sparsematrix = csc_matrix(sparsematrix)
sparsematrix = sparsematrix.asfptype()

print('finished making sparse matrix')
u, s, vt = svds(sparsematrix, k=100)
print(s)
