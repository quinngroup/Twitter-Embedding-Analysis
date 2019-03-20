print("importing..")
import numpy as np
from joblib import Parallel, delayed
import csv, re, os
from itertools import combinations
from collections import defaultdict
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
print("finished importting")

def load_corp(file):
    ind = 0
    data = []
    with open(file) as f:
        for line in f:
            tweet = line.lower() # lowercase

            tweet = re.sub(r"http\S+", "", tweet) # removes urls
            tweet = re.sub(r"@\S+","",tweet)      # removes usernames
            tweet = re.sub(r"#\S+","",tweet)      # removes hastags
            tweet = re.sub('[\W_]+',' ', tweet)   # removes various non-alphanumeric characters
            tweet = re.sub(r"rt","",tweet)        # removes retweet 'rt'

            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(tweet)
            filtered_sentence = [w for w in word_tokens if not w in stop_words] # removes stopwords


            tweet = ' '.join(filtered_sentence)
            # adds tweet to list
            data.insert(ind,tweet)

            ind+=1
    data = list(filter(None, data)) # removes any empty entrie
    return data

def dd():
    return defaultdict(int)

def cmb(t,val):
    return list(combinations(t,val))

def counts(file, n, l=5):
    print("loading",file)
    corp = load_corp("../dicts/"+file)
    print("loaded", file)
    wc = dd()
    wnd = dd()
    print("creaated wc, wnd")
    # increments values
    for tweet in corp:
        tweet = tweet.split()
        opt = cmb(tweet,2)

        for i in range(len(tweet)):
            wc[tweet[i]]+=1
            if i < len(tweet) - 5:
                a = tweet[i:i+5]

                for j in range(len(opt)):
                    wnd[opt[j]]+=1

    wc = pd.DataFrame(wc, index=[0])
    wnd = pd.DataFrame(wnd, index=[0])
    wc = wc.T
    wnd = wnd.T

    wc.to_csv("wc/wc" + str(n) + ".csv")
    wnd.to_csv("wnd/wnd" + str(n) + ".csv")

print("start")
path = "/opt/data/dicts"
dir_list = os.listdir(path)
for f, n in enumerate(dir_list):
    print(n, f)
    counts(n, f)
