import scipy
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE as tsne
import seaborn as sns

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

pca = PCA(n_components=2000)
pca.fit(sparsematrix)
X_pca = pca.transform(sparsematrix)
print("completed pca")

tsne_results = tsne(n_components=2, verbose=1).fit_transform(X_pca)
print("completed tsne")

#arr = list(tsnedata.T)
#x = tsne_results[:,0]
#x = [number**3 for number in x]
#y = tsne_results[:,1]
#y = [number**3 for number in y]


#fig = plt.figure()
#ax = fig.gca(projection='3d')
#fig, ax = plt.subplots()
#ax.set(xlim = (0,20), ylim = (-500, 1000))
#ax.scatter(x, y)

#for i in range(0, 3000):
#    label = listofwords[i]
#    ax.text(x[i], y[i],  label)
#    ax.annotate(txt, (x[i], y[i], z[i]))
df_subset = pd.DataFrame(columns=['tsne-2d-one', 'tsne-2d-two'])
df_subset['tsne-2d-one'] = tsne_results[:,0]
df_subset['tsne-2d-two'] = tsne_results[:,1]
plt.figure(figsize=(16,10))
sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    hue="y",
    palette=sns.color_palette("hls", 10),
    data=df_subset,
    legend="full",
    alpha=0.3
)

plt.savefig('../../reorganized_data/cluster1/tsneplot.png')

print("Completed")

#Future Ideas/steps:
    #Scale the values out to the 15th power and then view it and scale it back down
    #SVD first then PCA on SVD
