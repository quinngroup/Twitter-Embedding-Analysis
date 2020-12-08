import pandas as pd
from numpy import linalg
import numpy as np

df = pd.read_csv('../../reorganized_data/cluster1/ppmi_matrix11.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.set_index('word')
df = df.replace([np.inf,-np.inf],np.nan).fillna(0)
mat = np.array(df, dtype="float")
print(mat.shape)
print(np.isnan(mat).any())
print(np.isinf(mat).any())
print(df.dtypes)
u, s, vh = linalg.svd(mat)
print(u.shape)
print(s.shape)
print(vh.shape)
