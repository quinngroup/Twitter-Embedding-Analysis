import pandas as pd
from pandas import DataFrame
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import os
import glob


# imports from count_data.py
import argparse
from functools import reduce
import gzip
import json
from pathlib import Path

from joblib import delayed, Parallel


pd.set_option('display.max_columns', None)
#nltk.download('all') Only do this on first run

english_stopwords = stopwords.words('english') 

def get_data():

    '''Returns a list of the relative filepaths of all of the twitter data we are using.
    This makes collaboration easy, because the filepaths should be the same for all of us.

    Returns: List of relative filepaths of Trump Data.

    '''

    return(glob.glob('../../../opt/data/twitter/*'))

def create_data_frame(file_path):
    
    '''Creates a dataframe of the filepath passed in.

    Keyword arguments:
    file_path -- file path to file that we are creating a dataframe for
    
    Returns: df (a df of the smaller json)

    '''
    
    with open(file_path) as json_file:
        df = pd.read_json(json_file)
        return df
      
def preprocess_tweet(tweet):
    
    '''Does simple preprocessing on the df passed in. Used by clean_dataframe().

    Keyword arguments:
    tweet -- the single tweet that is passed in, contains the twitter json data.
    
    Returns: a preprocessed tweet

    '''
    
    #print('Raw tweet: ', tweet, '\n')
    tweet_without_rt = re.sub('RT', '', tweet)
    tweet_without_hyperlinks = re.sub(r'https?:\/\.*\/\w*', "", tweet_without_rt)
    tweet_without_hashtags = re.sub(r'#\w*', '', tweet_without_hyperlinks)
    # This general process will continue until it's something we like

    return tweet_without_hashtags

def tokenize(cleaned_tweet):
    '''Tokenizes the tweet passed in. Also removes stop words.

    Keyword arguments:
    cleaned_tweet -- the cleaned tweet.  

    returns a token

    '''

    tweet_tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
    tweet_list = tweet_tokenizer.tokenize(cleaned_tweet)

    tweet_list_no_stopwords = [i for i in tweet_list if i not in english_stopwords]

    return tweet_list_no_stopwords


def clean_dataframe(passed_dataframe):
    '''Calls preprocess_tweet on all the tweets within the dataframe that is passed into the function.
    Uses preprocess() and then tokenize().

    Keyword arguments:
    passed_dataframe -- the dataframe this wants to be done on

    '''

    for tweet in passed_dataframe['tweet_text']:
        #print('TWEET: ', tweet, '\n')
        
        print('PREPROCESSED TWEET: ', preprocess_tweet(tweet), '\n')
        
        #print('TOKENIZED LIST: ', tokenize(preprocess_tweet(tweet)), '\n')


########## Sort data by Date (Making dictionary by week (or timespan requested) #################

    ''' We are currently planning on storing dataframes in a single dictionary. Each key is a date and each keyvalue corresponds to that respective
        date's dataframe.
    '''

#################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Twitter Download Validation',
        epilog = 'lol moar tweetz', add_help = 'How to use',
        prog = 'python count_data.py -i <inputdir>')
    parser.add_argument('-i', '--inputdir', required = True,
        help = 'Path directory containing the json gzipped data.')

    args = vars(parser.parse_args())
    path = Path(args['inputdir'])

    # Get the list of data files.
    file_list = list(path.glob("*.json.gz"))
    print(f"Found {len(file_list)} files.")

    for x in range(1):
        current_df = create_data_frame(x)
        clean_dataframe = clean_dataframe(current_df)
        print(clean_dataframe)        

    '''
    # Go through each one and preprocess.
    out = Parallel(n_jobs = -1)(
        delayed(examine_file)(f)
        for f in file_list)
    

    results = list(reduce(lambda x, y: [x[0] + y[0], x[1] + y[1], x[2] + y[2]], out))
    '''
