import numpy as np
import pandas as pd
import xarray as xr
import os, re, json
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
            #print("==============TWEET==============")
            #print("Original Tweet:",line)
            #print("\n")

            words = line.split()

            # removes usernames from the list
            for word in words:
                if re.match(r'^@',word):
                    words.remove(word)
            #        print("removed word",word)

            line = ' '.join(words)

            # gensim preproceesing...
            # makes lowercase, strips punctuation, and removes stopwords
            CUSTOM_FILTERS = [lambda x: x.lower(), remove_stopwords]
            words = preprocess_string(line,CUSTOM_FILTERS)
            #print("preprocessing complete:",words)

            # removes usernames from the list
            for word in words:
                if re.match(r'^@',word):
                    words.remove(word)
             #       print("removed word",word)

            # removes RT from the begining of retweets
            if "rt" in words:
                words.remove("rt")
            #    print("removed rt")


            # removes urls from the list
            for word in words:
                if re.match(r'^http',word):
                    words.remove(word)
            #        print("removed url",word)

            # checks to see if words are in data and if not adds the word to data
            for word in words:
                if word in data:
                    continue
                else:
            #        print(word,"added to list")
                    data[str(word)] = ind
                    ind+=1

# dumps data to file and saves it
with open("voc.json", "w") as fp:
  json.dump(data, fp)
print("written to json file")
