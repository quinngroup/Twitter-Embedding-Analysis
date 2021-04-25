import scipy
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs
import pandas as pd
import numpy as np

A = np.random.rand(20,20)
U, s, VT = svds(A, k=10)
print('finished making sparse matrix')
print(U)
print(s)
print(VT)
print(U.shape)
print(s.shape)
print(VT.shape)

