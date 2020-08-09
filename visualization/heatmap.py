import numpy as np
import pandas as pd
import seaborn as sns
import scipy
import  matplotlib.pyplot as plt

filled = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
filled = filled.loc[:, ~filled.columns.str.contains('^Unnamed')]
listofwords = filled['word'][0:500].to_list()
print(listofwords)

print('created list')
filled = filled.set_index('word')
filled = filled.reset_index().dropna().set_index('word')

sparsematrix = filled.to_numpy()
shortsparsematrix = sparsematrix[0:500, 0:500]
print('starting to make heatmap')

plt.subplots(figsize=(100,100))
heatmap = sns.heatmap(shortsparsematrix, vmax=100, xticklabels = listofwords, yticklabels = listofwords)
print('finished creating heatmap')
heatmap.get_figure().savefig('shortsparseheatmap8.png')
print(':D')
