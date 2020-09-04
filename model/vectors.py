import scipy
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#SVD Attempt:

filled = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
filled = filled.loc[:, ~filled.columns.str.contains('^Unnamed')]
listofwords = filled['word'][0:6000].to_list()
print(listofwords)
print(len(listofwords))

print('created list')
filled = filled.set_index('word')
filled = filled.reset_index().dropna().set_index('word')

sparsematrix = filled.to_numpy()
#sparsematrix = csc_matrix(sparsematrix)
#sparsematrix = sparsematrix.asfptype()

#print('finished making sparse matrix')

#u, s, vt = svds(sparsematrix, k=100)
#print(u.shape)
#print(vt.shape)
#print(u.shape[1])
#print(vt.shape[0])
#true_s = np.zeros((u.shape[1], vt.shape[0]))
#true_s[:s.size, :s.size] = np.diag(s)
#print(true_s)
#print(true_s.shape)
#np.save('../../reorganized_data/cluster1/sparse_matrix', true_s)



#PCA Attempt:

pca = PCA(n_components=2)
pca.fit(sparsematrix)
X_pca = pca.transform(sparsematrix)

print(X_pca.shape)

arr = list(X_pca.T)
x = arr[0]
x = [number**3 for number in x]
y = arr[1]
y = [number**3 for number in y]
#z = arr[2]
#z = [number**10 for number in z]

#fig = plt.figure()
#ax = fig.gca(projection='3d')
fig, ax = plt.subplots()
ax.set(xlim = (0,20), ylim = (-500, 1000))
ax.scatter(x, y)

for i in range(0, 3000):
    label = listofwords[i]
    ax.text(x[i], y[i],  label)
#    ax.annotate(txt, (x[i], y[i], z[i]))

plt.savefig('../../reorganized_data/cluster1/pcaplot.png')

print("Completed")

#Future Ideas/steps:
    #Scale the values out to the 15th power and then view it and scale it back down
    #SVD first then PCA on SVD
