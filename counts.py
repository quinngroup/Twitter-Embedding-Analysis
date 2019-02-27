import numpy as np
from joblib import Parallel, delayed
import csv, re
from itertools import combinations
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')


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

def counts(corp,l=5):
    wc = defaultdict(int)
    wnd = defaultdict(int)

    # increments values
    for tweet in corp:
        tweet = tweet.split()
        opt = list(combinations(tweet,2))

        for i in range(len(tweet)):
            wc[tweet[i]]+=1
            if i < len(tweet) - 5:
                a = tweet[i:i+5]

                for j in range(len(opt)):
                    wnd[opt[j]]+=1

    # writes word count to a file
    with open('wc1.csv', 'w') as f:
        w = csv.DictWriter(f, wc.keys())
        w.writeheader()
        w.writerow(wc)

    # writes window count toa file
    with open('wnd1.csv', 'w') as f:
        w = csv.DictWriter(f, wnd.keys())
        w.writeheader()
        w.writerow(wnd)

print("loading corp")
corp = load_corp("test.txt")
print("corp loaded")
counts(corp)
