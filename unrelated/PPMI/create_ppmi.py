import os, math
import dask.dataframe as dd
import pandas as pd
import numpy as np
from scipy.sparse import lil_matrix, vstack, save_npz
from os import listdir
from os.path import isfile, join

masterx2i, masteri2x = {}, {}
counter = 0



def iter_ppmi():
    mypath = './wc2'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i,j in enumerate(onlyfiles):
        fname = j[3:-4]
        createDict(fname)
        wc = pd.read_csv("./wc2/wc_"+fname+".csv", index_col=0)
        wnd = pd.read_csv("./wnd2/wnd_"+fname+".csv", index_col=0)
        ppmi = createMat(wc, wnd, fname)


def createDict(file_name):
    global counter
    print(file_name)
    wc = pd.read_csv("wc2/wc_"+file_name+'.csv', index_col=0)
    wc.columns = ["word", "count"]
    # print(wc)
    for index, row in wc.iterrows():

        if row["word"] not in masterx2i.keys():
            masterx2i[row["word"]] = counter
            masteri2x[counter] = row["word"]
            counter = counter+1
            
    print("finished creating dicts")
            

def delete_row_lil(mat, i):
    if not isinstance(mat, lil_matrix):
        raise ValueError("works only for LIL format -- use .tolil() first")
    mat.rows = np.delete(mat.rows, i)
    mat.data = np.delete(mat.data, i)
    mat._shape = (mat._shape[0] - 1, mat._shape[1])
    
def createMat(wc, wnd,fname):
    
    curr_mat = lil_matrix(np.zeros((1,len(masterx2i)))) 
    
    for index, word1 in masteri2x.items():
        
        if index % 100 == 0:
            print(f'finished creating {index/len(masterx2i):.2%} of ppmi')
        
        temp_row = np.zeros((1,len(masterx2i))) # the row in ppmi matrix
        
        for i in range(len(masteri2x)):
            
            word2 = masteri2x[i]
            
            wc1row = wc.loc[wc['0']==word1].values.tolist()
            wc2row = wc.loc[wc['0']==word2].values.tolist()
            #print(wc1row)
            wc1 = wc1row[0][4]   # word count word1
            wc2 = wc2row[0][4]   # word count word2
            
            
            wndw1q = wnd.loc[wnd['0']==word1]
            wndw2q = wndw1q.loc[wndw1q['1']==word2].values.tolist() # gets row for window count     
            try:
                wndc = wndw2q[0][3]
            except IndexError:    # if the words do not occur together then ppmi val should be 0
                temp_row[0][i] = 0
                break
            
            top = wndc * len(masteri2x)
            bot = wc1 * wc2
            val = math.log(float(top/bot),2) # calculate ppmi val
            
            if val < 0:
                val = 0
                
            temp_row[0][i] = val
            # print(val)
            
        sm_temp = lil_matrix(temp_row)
        curr_mat = vstack([curr_mat, sm_temp]) # stacks rows in top of each other
        #print("added row")
        
    delete_row_lil(curr_mat.tolil(), [-1])
    save_npz("./mats/ppmi"+fname+".npz", curr_mat)
    return curr_mat

iter_ppmi()