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

def create_dataframe(file_path):
    
    '''Creates a dataframe of the filepath passed in.

    Keyword arguments:
    file_path -- file path to file that we are creating a dataframe for
    
    Returns: df (a df of the smaller json)

    '''
    
    df = pd.read_json(file_path, compression='gzip', lines=True)
    return df
    
def preprocess_tweet(tweet):
    
    '''Does simple preprocessing on the df passed in. Used by clean_dataframe().
       Credit for tweet_without_hyperlinks and tweet_without_hyperlinks2 RegEx can be found at <a href="URL">https://stackoverflow.com/questions/720113/find-hyperlinks-in-text-using-python-twitter-related</a>

    Keyword arguments:
    tweet -- the single tweet that is passed in, contains the twitter json data.
    
    Returns: a preprocessed tweet

    '''

    if isinstance(tweet, float):
        print('Empty Tweet')
    else:
        #print(type(tweet))
        print('Raw tweet: ', tweet, '\n')
        tweet_without_rt = re.sub('RT', '', tweet)
        tweet_without_hyperlinks = re.sub(r'(http://[^ ]+)', "", tweet_without_rt)
        tweet_without_hyperlinks2 = re.sub(r'(https://[^ ]+)', "", tweet_without_hyperlinks)
        tweet_without_punctuation = re.sub('[.#,!?*]', '', tweet_without_hyperlinks2)
        tweet_without_at = re.sub('@\w*', "", tweet_without_punctuation)
        # This general process will continue until it's something we like
        
        return tokenize(tweet_without_at)

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

def clean_dataframe(passed_dataframe):
    '''Calls preprocess_tweet on all the tweets within the dataframe that is passed into the function.
    Uses preprocess() and then tokenize().

    Keyword arguments:
    passed_dataframe -- the dataframe this wants to be done on

    '''
    
    for tweet in passed_dataframe['text']:
        #print('TWEET: ', tweet, '\n')
        print('PREPROCESSED TWEET (And now tokenized): ', preprocess_tweet(tweet), '\n')
        #print('TOKENIZED LIST: ', tokenize(preprocess_tweet(tweet)), '\n')
        
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

    for x in range(10):
        current_df = create_dataframe(file_list[x])
        clean_dataframe(current_df)
