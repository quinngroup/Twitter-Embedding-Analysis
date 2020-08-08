import numpy as np 
import pandas as pd
import seaborn as sns

filled = pd.read_csv('../../reorganized_data/cluster1/filled_matrix.csv')
filled = filled.loc[:, ~filled.columns.str.contains('^Unnamed')]
filled = filled.set_index('word')
filled = filled.reset_index().dropna().set_index('word')

heatmap = sns.heatmap(filled, annot=True, square=True)
heatmap.savefig('../../reorganized_data/cluster1/heatmap.png')
