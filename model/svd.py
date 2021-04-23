import pandas as pd
from numpy import linalg
import numpy as np

df = pd.read_csv('../../reorganized_data/cluster0/filled_matrix.csv', index_col="word_set")
mat = np.array(df, dtype="float")
print(mat.shape)
print(np.isnan(mat).any())
print(np.isinf(mat).any())
print(df.dtypes)
u, s, vh = linalg.svd(mat)
print(u.shape)
print(s.shape)
print(vh.shape)
