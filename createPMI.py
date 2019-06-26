import numpy as np
import gensim as gn
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation, preprocess_string
from scipy.sparse import csc_matrix, save_npz, lil_matrix
import json
import os, re, math
import multiprocessing as mp
import pandas as pd
from IPython.display import clear_output
from time import time
from collections import Counter
from math import log
# import pdb; pdb.set_trace()

wnd = pd.read_csv("testing/wnd0.csv")

wc = pd.read_csv("testing/wc0.csv")

x2i, i2x = {}, {}
for indexes, actualrowvalues in wc.iterrows():
    x2i[actualrowvalues["word"]] = indexes
    i2x[indexes] = actualrowvalues["word"]
    
wndSum = wnd['counts'].sum()
wcSum = wc['counts'].sum()

pmi_samples = Counter()
data, rows, cols = [], [], []

for index, rowvalues in wnd.iterrows():
    
    if index % 10000 == 0:
        print(f'finished {index/20427230:.2%} of the PMI matrix')

    rows.append(x2i[rowvalues["word1"]])
    cols.append(x2i[rowvalues["word2"]])
    targetrow = wc.loc[wc["word"] == rowvalues["word1"]]
    targetrow2 = wc.loc[wc["word"] == rowvalues["word2"]]
    data.append(np.log((rowvalues["counts"] / wndSum) / (targetrow["counts"] / wcSum) / (targetrow2["counts"] / wcSum)))
    pmi_samples[(rowvalues["word1"], rowvalues["word2"])] = data[-1]
PMI = csc_matrix((data, (rows, cols)))
save_npz("../matrices/PMI_0.npz", PMI)
