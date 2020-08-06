import pandas as pd
from pandas import DataFrame
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import os
import glob
import dask.dataframe as dd
import shutil

# imports from count_data.py
import argparse
from functools import reduce
import gzip
import json
from pathlib import Path

from joblib import delayed, Parallel

# pd options to for cleaner output

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
#pd.set_option('display.max_colwidth', -1)

#nltk.download('all') Only do this on first run

english_stopwords = set(stopwords.words('english'))

def get_data(path):

    '''Returns a list of the relative filepaths of all of the twitter data we are using.
    This makes collaboration easy, because the filepaths should be the same for all of us.

    Returns: List of relative filepaths of Trump Data.

    '''

    path = Path(path)
    # Get the list of data files.
    file_list = list(path.glob("*.json.gz"))
    print(f"Found {len(file_list)} files.")

    return file_list

def preprocess_tweet(tweet):
    
    '''Does simple preprocessing on the df passed in. Used by clean_dataframe().
       Credit for some of the patterns (RegEx) can be found at <a href="URL">https://stackoverflow.com/questions/720113/find-hyperlinks-in-text-using-python-twitter-related</a>

    Keyword arguments:
    tweet -- the single tweet that is passed in, contains the twitter json data.
    
    Returns: a preprocessed tweet

    '''

    if isinstance(tweet, float):
        print('Empty Tweet')
    else:
        #print(type(tweet))
        #print('Raw tweet: ', tweet, '\n')
        patterns = ('RT', r'(http://[^ ]+)', r'(https://[^ ]+)', '[.#,!?*"”“:/()]', '@\w*')
        tweet_final = re.sub(r'|'.join(patterns), "", tweet)
        # This general process will continue until it's something we like
        
        return tokenize(tweet_final)

def tokenize(cleaned_tweet):
    '''Tokenizes the tweet passed in. Also removes stop words. Used by clean_dataframe(). Also used by preprocess_tweet().

    Keyword arguments:
    cleaned_tweet -- the cleaned tweet.  

    returns a token

    '''
    if isinstance(cleaned_tweet, float):
        print('Empty Tweet')
    else:
        tweet_tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
        tweet_list = tweet_tokenizer.tokenize(cleaned_tweet)
        tweet_list_no_stopwords = [i for i in tweet_list if i not in english_stopwords]
        
        return tweet_list_no_stopwords

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Twitter Download Validation',
        epilog = 'lol moar tweetz', add_help = 'How to use',
        prog = 'python preprocessing_datavis.py -i <inputdir>')
    parser.add_argument('-i', '--inputdir', required = True,
        help = 'Path directory containing the json gzipped data.')

    args = vars(parser.parse_args())
    path = Path(args['inputdir'])

    # Get the list of data files.
    file_list = list(path.glob("*.json.gz"))
    print(f"Found {len(file_list)} files.")

    # For each file in Twitter Data, make a clean pd dataframe and add to a giant dask df.

    for x in range(10):
        current_df = create_dataframe(file_list[x])
        clean_dataframe(current_df)

        #Line below should insert each pd dataframe created from clean_dataframe into the overarching dask system
        #[clean_dataframe(current_df)]

