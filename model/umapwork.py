import scipy
import pandas as pd
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE as tsne
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import umap
from adjustText import adjust_text

filled = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
filled = filled.loc[:, ~filled.columns.str.contains('^Unnamed')]
listofwords = filled['word'][0:6000].to_list()
print(listofwords)
print(len(listofwords))

print('created list')
filled = filled.set_index('word')
filled = filled.reset_index().dropna().set_index('word')

sparsematrix = filled.to_numpy()
reducer = umap.UMAP(min_dist=0.25,n_neighbors=10)
print('UMAP model finished')

scaled_sparsematrix = StandardScaler().fit_transform(sparsematrix)
embedding = reducer.fit_transform(scaled_sparsematrix)
print(embedding.shape)
x = embedding[:,0]
#x = [number**5 for number in x]
print('completed x')
y = embedding[:,1]
#y = [number**5 for number in y]
print('points created (completed y)')

fig, ax = plt.subplots(figsize=(48,36))
ax.scatter(x,y,s=1)
print('plot created')

texts = [ax.text(x[i], y[i], listofwords[i]) for i in range(1000)]
adjust_text(texts)
print('text adjusted')

plt.savefig('../../reorganized_data/cluster1/umapplot.png')

print('Completed')


