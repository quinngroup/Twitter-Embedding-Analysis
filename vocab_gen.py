import numpy as np
import pandas as pd
import xarray as xr
import os, re
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation, preprocess_string

# CLEANING TIME
path = "/opt/data/dicts"
dicts_list = os.listdir(path)
data = {}
ind = 0

for file in dicts_list:
    with open("../dicts/"+file) as f:
        print("opened: ../dicts/"+file)
        for line in f:
            print("line:",line)
            #splits line into words in a list
            words = line.split()
            print("line split:",words)

            # removes RT from the begining of retweets
            if "RT" in words:  words.remove("RT")

            # removes urls from the list
            for word in words:
                if word.startsWith("http"):
                    words.remove(word)

            # usues gensim preprocessing to remove punctuation, stopwords and make the words lowercase
            CUSTOM_FILTERS = [lambda x: x.lower(), strip_punctuation, remove_stopwords]
            words2 = preprocess_string(words,CUSTOM_FILTERS)
            print("preprocessing complete:",words2)

            # checks to see if words are in data and if not adds the word to data
            for word in words2:
                if word in data:
                    continue
                else:
                    print(word,"added to list")
                    dict[str(word)] = ind
                    ind+=1

# dumps data to file and saves it 
js = json.dump(data)
f = open("voc.json","w")
f.write(js)
print("written to json file")
f.close()
