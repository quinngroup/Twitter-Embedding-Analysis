import pandas as pd
from numpy import linalg
import numpy as np

df = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.set_index('word')
mat = np.array(df, dtype="float")
print(mat.shape)
u, s, vh = linalg.svd(mat)
print(u.shape)
print(s.shape)
print(vh.shape)
