import json
import pandas as pd
from pandas import DataFrame
import nltk
import re

################### Globally Setting Values ##############################
pd.set_option('display.max_columns', None)
#testing to add to branch


def create_df():
    with open('tweets3506.json') as json_file:
        pandaDf = json.load(json_file)

def to_data_frame():
    with open('../../tweets245.json') as json_file:
        df = pd.read_json(json_file)
      
#currently removing punctuation, lowercase letters, remove numbers

def preprocess(data):
    replace_no_space = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    replace_with_space = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)|(\x97)")

    clean_data = [replace_no_space.sub("", line.lower()) for line in data]
    clean_data = [replace_with_space.sub(" ", line) for line in data]

    return clean_data



########## Sort data by Date (Making CSVs by week) #################










######## Tokenization, preparation for Matrix #####################

#tokenizing into words, removing stop words (bag of words model)
#def tokenize_data():
    # placeholder again

#I'm not entirely sure the structure of the PMI matrix, but the data is now sent to that file




########### Main ################################################



if __name__ == "__main__":
    print(preprocess(to_data_frame()))
    print(return_tweets(to_data_frame()))
