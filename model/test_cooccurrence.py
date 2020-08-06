import numpy as np
import pandas as pd

df = pd.read_csv('../reorganized_data/cluster1/filled_matrix.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.set_index('word') # Changing index from nums to words
df = df.reset_index().dropna().set_index('word') # changing index from nums to words

print(df.columns)
print(df)
print(df.shape)

df2 = df.transpose()
print(df.equals(df2))

nparray = df.values

def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)

print(check_symmetric(nparray))
