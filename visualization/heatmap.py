import numpy as np
import pandas as pd
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

filled = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv', index_col="word_set")
listofwords = filled['word'][0:6000].to_list()
print(listofwords)

print('created list')

sparsematrix = filled.to_numpy()
shortsparsematrix = sparsematrix[0:6000, 0:6000]
print('starting to make heatmap')

plt.subplots(figsize=(100,100))
heatmap = sns.heatmap(shortsparsematrix, vmax=100, xticklabels = listofwords, yticklabels = listofwords)
print('finished creating heatmap')
heatmap.get_figure().savefig('heatmap422021.png')
print(':D')
