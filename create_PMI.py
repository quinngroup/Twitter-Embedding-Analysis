from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation, preprocess_string
from scipy.sparse import lil_matrix, save_npz
import json
import os, re, math
import multiprocessing as mp
from decimal import *

def load_voc():
    with open("voc.json","r") as js:
        data = json.load(js);
        res = dict((v,k) for k,v in data.items())
    return res

def load_corp(file):
    ind = 0
    data = []
    with open("../dicts/"+file) as f:
        for line in f:
            words = line.split()

            # removes usernames from the list
            for word in words:
                if re.match(r'^@',word):
                    words.remove(word)

            line = ' '.join(words)

            # gensim preproceesing...
            # makes lowercase, strips punctuation, and removes stopwords
            CUSTOM_FILTERS = [lambda x: x.lower(), remove_stopwords]
            words = preprocess_string(line,CUSTOM_FILTERS)

            # removes usernames from the list
            for word in words:
                if re.match(r'^@',word):
                    words.remove(word)

            # removes RT from the begining of retweets
            if "rt" in words:
                words.remove("rt")

            # removes urls from the list
            for word in words:
                if re.match(r'^http',word):
                    words.remove(word)

            line = ' '.join(words)

            # adds tweet to list
            data.insert(ind,line)
            ind+=1
    return data


voc = load_voc()
print("vocabulary loaded")
len_voc = len(voc)
corp = load_corp("../dicts/2018-01-22.txt")
print("corpus loaded")

PMI = lil_matrix((len_voc, len_voc)) # scipy sparse matrix

for i in range(0,len_voc):
    for j in range(0,len_voc):
        wd1_cnt = wd_count(voc[i],corp) # word 1 count
        wd2_cnt = wd_count(voc[j],corp) # word 2 cout
        wnd_cnt = wd_count_wnd(voc[i],voc[j],corp,5) # window count

        top = wnd_cnt * len_voc
        bot = wd1_cnt * wd2_cnt

        if top > 0 and bot > 0:
            tot = top/bot

            # One of the words may not occur in the corpus
            # if thats so then we can ignore the value because
            # it will be 0
            if wd1_cnt > 0 and wd2_cnt > 0 and tot >0:
                res = Decimal(math.log(top/bot))
                print("added: PMI["+voc[i]+","+voc[j]+"] = ",res)
                PMI[i,j] = res

save_npz("2018-01-22.npz", PMI) # saves matrix
