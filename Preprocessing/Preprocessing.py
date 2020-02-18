import json
import pandas as pd
from pandas import DataFrame

def json_print():
    with open('tweets3506.json') as json_file:
        data = json.load(json_file)
        for x in range(0, 50):
            print(data[x])

def panda_json():
    with open('/data/tweets3506.json') as json_file:
        pandaDf = json.load(json_file)
    for element in pandaDf:
        print(element['tweet_text'])

#currently removing punctuation, lowercase letters, remove numbers
#def clean_data():
    #placeholder

#tokenizing into words, removing stop words (bag of words model)
#def tokenize_data():
    # placeholder again
#I'm not making the ppi term matrix, but this is where it would be done

if __name__ == "__main__":
    #json_print()
    panda_json()
