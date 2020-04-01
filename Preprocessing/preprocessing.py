import json
import pandas as pd
from pandas import DataFrame
import nltk
import re

pd.set_option('display.max_columns', None)

def create_data_frame(file_path):
    
    '''Creates a dataframe of the filepath passed in.

    Keyword arguments:
    file_path -- file path to file that we are creating a dataframe for
    
    Returns: df

    '''
    
    with open(file_path) as json_file:
        df = pd.read_json(json_file)
        return df
      
def preprocess(data):
    
    '''Does simple preprocessing on the df passed in.

    Keyword arguments:
    data -- dataframe that is passed in, contains the twitter json data.
    
    Returns: df

    '''

    replace_no_space = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    replace_with_space = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)|(\x97)")

    clean_data = [replace_no_space.sub("", line.lower()) for line in data]
    clean_data = [replace_with_space.sub(" ", line) for line in data]

    print(type(clean_data))

    return clean_data



########## Sort data by Date (Making dictionary by week (or timespan requested) #################

 '''
 We are currently planning on storing dataframes in a single dictionary. Each key is a date and each keyvalue corresponds to that respective
 date's dataframe.
 '''




######## Tokenization, preparation for Matrix #####################

 '''
 this probably isn't necessary
 '''


########### Main ################################################



if __name__ == "__main__":
    current_df = create_data_frame('../tweets245.json')
    #print(current_df)
    print(preprocess(current_df))
