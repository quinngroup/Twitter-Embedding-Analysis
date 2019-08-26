import numpy as np
import gensim as gn
from scipy.sparse import csc_matrix, save_npz, lil_matrix
import json
import os, re, math
import multiprocessing as mp
import pandas as pd
from IPython.display import clear_output
from time import time
from collections import Counter
from math import log
import scipy.sparse.linalg as la
from multiprocessing import Pool
import pandas as pd
import multiprocessing as mp
from multiprocessing import cpu_count, Pool
from functools import partial
from numba import jit
import numpy as np
import os
import time
import csv
import scipy as sp
from scipy.sparse import *
from scipy import *
counter = 0
masterx2i, masteri2x = {}, {}

@jit
def createDicts(file_name):
    global counter
    print(file_name)
    wc = pd.read_csv("wc2/wc_"+file_name+'.csv')
    wc = wc.drop("Unnamed: 0", axis=1)
    wc.columns = ["word", "count"]
    print(wc)
    for index, row in wc.iterrows():
        if row["word"] not in masterx2i.keys():
            masterx2i[row["word"]] = counter
            masteri2x[counter] = row["word"]
            counter = counter+1
            print(counter)
            
@jit
def savei2x(i2x):
    w = csv.writer(open("i2x.csv", "w"))
    for key, val in i2x.items():
        w.writerow([key, val])

@jit        
def savex2i(x2i):
    w = csv.writer(open("x2i.csv", "w"))
    for key, val in x2i.items():
        w.writerow([key, val])
        wc_files = [f for f in os.listdir("wc2") if os.path.isfile(os.path.join("wc2", f))]
    for i in range(len(wc_files)):
        file_name = wc_files[i][-14:-4]
        createDicts(file_name)

savei2x(masteri2x)
savex2i(masterx2i)

i2xdf = pd.DataFrame(masteri2x.items(), columns=['Index', 'Word'])
x2idf = pd.DataFrame(masterx2i.items(), columns=['Word', 'Index'])

i2xdf.to_csv("i2xdf.csv")
x2idf.to_csv("x2idf.csv")

with open('i2x.csv') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

with open('x2i.csv') as csv_file2:
    reader2 = csv.reader(csv_file2)
    mydict2 = dict(reader2)

i2xdfread = pd.read_csv("i2xdf.csv")
x2idfread = pd.read_csv("x2idf.csv")

i2xdfread.to_csv("i2xdf.csv")
x2idfread.to_csv("x2idf.csv")

def createNewMatrices(matrix):
    largePPMI = sp.sparse.lil_matrix((len(x2idfread),len(x2idfread)), dtype=float16).toarray()
    loadedwc = pd.read_csv("./wc2/wc_"+matrix+".csv", index_col=0)
    loadedwnd = pd.read_csv("./wnd2/wnd_"+matrix+".csv", index_col=0)
    wndSum = loadedwnd['2'].sum()
    wcSum = loadedwc['1'].sum()
    for index, row in loadedwnd.iterrows():
        
        if index % len(loadedwnd) == 0:
            print(f'finished {index/len(wnd):.2%} of the PPMI matrix: '+file_name)
        
        word1 = row[0]
        word2 = row[1]
        
        wcselector1 = loadedwc.loc[loadedwc['0'] == word1]
        wcselector2 = loadedwc.loc[loadedwc['0'] == word2]
        w1count = wcselector1["1"]
        w2count = wcselector2["1"]
        
        word1selector = i2xdfread.loc[i2xdfread['Word'] == word1]
        word2selector = i2xdfread.loc[i2xdfread['Word'] == word2]
        indexforword1 = int(word1selector["Index"])
        indexforword2 = int(word2selector["Index"])
        
        value1 = float((row[2] / wndSum))
        value2 = float((w1count / wcSum))
        value3 = float((w2count / wcSum))
        
        value4 = float(value1/value2)
        
        prePPMI = float(value4/value3)
        
        PPMIvalue = math.log(prePPMI,2)
        
        largePPMI[indexforword2][indexforword1] = PPMIvalue
        largePPMI[indexforword1][indexforword2] = PPMIvalue
        save_npz("../updatedmatrices/UpdatedPPMI_"+matrix+".npz", largePPMI)
        print(matrix+" finished creating")

oldwnd = [f for f in os.listdir("./wnd2") if os.path.isfile(os.path.join("./wnd2", f))]
for i in range(len(oldwnd)):
    matrix_name = oldwnd[i][-14:-4]
    createNewMatrices(matrix_name)
