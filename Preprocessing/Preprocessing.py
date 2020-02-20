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


########### Important Methods ########################################

def to_data_frame():
    with open('../../tweets245.json') as json_file:
        df = pd.read_json(json_file)
        #df.to_csv('csv_file.csv', encoding='utf-8', index=False)
    return df

def return_tweets(df):
    return(df['tweet_text'][0:20])

#currently removing punctuation, lowercase letters, remove numbers
def preprocess(data):
    replaceNoSpace = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    replaceWithSpace = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)|(\x97)")

    cleanData = [replaceNoSpace.sub("", line.lower()) for line in data]
    cleanData = [replaceWithSpace.sub(" ", line) for line in data]

    return cleanData



########## Sort data by Date (Making CSVs by week) #################










######## Tokenization, preparation for Matrix #####################

#tokenizing into words, removing stop words (bag of words model)
#def tokenize_data():
    # placeholder again

#I'm not entirely sure the structure of the PMI matrix, but the data is now sent to that file




########### Main ################################################



if __name__ == "__main__":
    #print(to_data_frame())
    print(return_tweets(to_data_frame()))
