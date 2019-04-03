import numpy as np
import gensim as gn
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation, preprocess_string
from scipy.sparse import csc_matrix, save_npz, lil_matrix
import json
import os, re, math
import multiprocessing as mp
import pandas as pd

wc = pd.read_csv("wc/wc0.csv")
wc.columns = {"words", "counts"}
print("loaded wc")

wnd = pd.read_csv("wnd/wnd0.csv")
wnd.columns = {"word1", "word2", "count"}
wnd.rename(columns={"count": "word1", "word1": "word2", "word2":"counts"}, inplace=True)
print("loaded wnd")

def sum_dict(d):
    # Finds the total word count
    s = 0
    for i in range(len(d["words"])):
        s = s + d["counts"][i]
        # print(d["counts"][i])
    return s


def create_PMI(wc, wnd):
    """
    Creates PMI matrix based on inputed wc and wnd
    
    Parameters:
    wc - word count dataframe
    wnd - window count dataframe
    
    Output:
    A PMI matrix
    """
    len_d = sum_dict(wc) # gets number of words
    
    len_wc = len(wc) # cut down a little on run time by only calculating value once
    
    PMI = csc_matrix((len_wc, len_wc),dtype=float) # scipy sparse matrix
    #print("created csc_matrix")
    
    for x in range(len_wc):
        for y in range(len_wc):
            try: # attempts to add element to PMI matrix 
                wnd_value_count = wnd[wnd.word1==wc["words"][y]][wnd.word2==wc["words"][x]]["counts"]
                #print("wnd count found")
                
                t = wnd_value_count * len_d
                b = wc["counts"][y] * wc["counts"][x]
                fin = math.log(t/b)
                PMI[x, y] = fin # final value is added to PMI
                print("PMI["+str(wc["words"][y])+","+str(wc["words"][x])+"] = "+str(fin)) # error checking
            except KeyError: # if element is not in wnd then it can be ignored
                print("Key Error:", y, x)
    save_npz("../matrices/PMI0.npz", PMI)
    return PMI


create_PMI(wc, wnd)

