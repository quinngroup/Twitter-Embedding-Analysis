import csv, re
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation, preprocess_string
from itertools import combinations

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

            # removes urls from the list
            for word in words:
                if re.match(r'^http',word):
                    words.remove(word)

            line = ' '.join(words)

            # gensim preproceesing...
            # makes lowercase, strips punctuation, and removes stopwords
            CUSTOM_FILTERS = [lambda x: x.lower(), remove_stopwords, strip_punctuation]
            words = preprocess_string(line,CUSTOM_FILTERS)

            # removes RT from the begining of retweets
            for i in range(len(words)):
                if "rt" == words[i]:
                    words.remove("rt")

            line = ' '.join(words)

            # adds tweet to list
            data.insert(ind,line)
            ind+=1
    return data

def counts(corp,l=5):
    wc = {}
    wnd = {}

    for tweet in corp:
        tweet = tweet.split()
        opt = list(combinations(tweet,2))
        for i in range(len(tweet)):
            wc[tweet[i]] = 0

        for i in range(len(opt)):
            wnd[opt[i]] = 0

        for i in range(len(tweet)):
            wc[tweet[i]]+=1
            if i < len(tweet) - 5:
                a = tweet[i:i+5]

                for j in range(len(opt)):
                    wnd[opt[j]]+=1

    with open('wc1.csv', 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, wc.keys())
        w.writeheader()
        w.writerow(wc)

    with open('wnd1.csv', 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, wnd.keys())
        w.writeheader()
        w.writerow(wnd)


corp = load_corp("../dicts/2018-01-22.txt")
counts(corp)
