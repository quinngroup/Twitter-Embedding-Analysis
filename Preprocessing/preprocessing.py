import json
import pandas as pd
from pandas import DataFrame
import nltk
import re

################### Globally Setting Values ##############################
pd.set_option('display.max_columns', None)




################# Test Methods ##########################################

# these are testing methods, don't worry about them
def json_print():
    with open('tweets3506.json') as json_file:
        data = json.load(json_file)
        for x in range(0, 50):
            print(data[x])

# these are testing methods, don't worry about them
def panda_json():
    with open('tweets3506.json') as json_file:
        pandaDf = json.load(json_file)
    for element in pandaDf:
        print(element['tweet_text'])

def return_tweets(df):
    return(df['tweet_text'][0:20])

def return_data(data):
    for line in data:
        print(line)

########### Important Methods ########################################

def to_data_frame():
    with open('../../tweets245.json') as json_file:
        df = pd.read_json(json_file)
        #df.to_csv('csv_file.csv', encoding='utf-8', index=False)
    return df

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
    #print(to_data_frame())
    print(preprocess(to_data_frame()))
    print(return_tweets(to_data_frame()))
