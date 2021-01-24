import new_preprocessing
import preprocessing

import os
import shutil
import pandas as pd
from pandas import DataFrame
import json
import gzip
from pathlib import Path
import csv
from operator import itemgetter

def move_data():
    
    '''This function separates our Twitter Data (originally in a single directory of 157345
    .json files) into 16 different directories (clusters) of data. The newly formed data
    is created in the current working directory in a folder entitled `reorganized_data`.
    This function will work correctly no matter where it is called. It is advised to 
    run this function outside of the git repo so the data is not mistakenly commited.
    
    '''

    file_list = new_preprocessing.get_data('../../../../data/twitterdata/')

    for x in range(16):
        dir_name = os.getcwd() + '/' + 'reorganized_data/' + 'cluster' + str(x + 1) + '/'

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)   
        
        for y in range(10000 * x, (10000 * x) + 10000):
            if y < len(file_list):
                shutil.copy(file_list[y], dir_name)      

def get_files_in_cluster(cluster_path):
    '''Returns a file_list of all the json files in a cluster.

    Keyword arguments:
    cluster_path -- file path to the cluster. e.g. "../../reorganized_data/cluster1/'
    
    Returns: file list of all the json files in a cluster.

    '''

    path = Path(cluster_path)
    file_list = list(path.glob("*.json.gz"))
    return file_list

def load_json(file_path):
    '''loads the specific file in a cluster into a dataframe. 

    Keyword arguments:
    cluster_path -- file path to cluster we are creating 
    
    Returns: the unprocessed data df.

    '''
    
    df = pd.read_json(file_path, compression='gzip', lines=True)
    df = df.dropna(how='all',thresh=4)
    df = df.reset_index(drop=True)
    return df

def preprocess_and_format_df(unprocessed_df, cluster_num):
    '''This function preprocesses the data found in a specific file and appends the jsons data to it's respective `cluster_data#.txt` if it exists. If not, it creates the file.

    Keyword arguments:
    unprocessed_df -- the unprocessed dataframe formed by load_json.
    cluster_num -- which cluster number is this operation being called on
    '''
    cluster_txt_file_path = "../../reorganized_data/cluster" + str(cluster_num) + "/cluster" + str(cluster_num) + "files.csv"

    # Creating the base file if it doesn't exist
#    if not os.path.isfile(cluster_txt_file_path):
 #       with open(cluster_txt_file_path, 'w') as csvfile:
  #          filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
   #         filewriter.writerow(['preprocessed tweet', 'date'])
    #        print('made new file')

  #  with open(cluster_txt_file_path, 'w') as csvfile:
   #     basefilewriter =  csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #    for tweet in unprocessed_df['text']:
     #       preprocessed_tweet = ' '.join(preprocessing.preprocess_tweet(tweet))
      #      basefilewriter.writerow([preprocessed_tweet])  



if __name__ == "__main__":
    #Run for first time
    #move_data()

    df = pd.DataFrame(columns=['created_at', 'text', 'preprocessed_text'])
    rootdir = '../../reorganized_data/cluster1'
    counter = 0
    for filename in os.listdir(rootdir):
        print("fname",filename)
        listoftweets = []
        with gzip.open(rootdir+"/"+filename, "r+") as f:
            #unpacked_f = load_json(f)
            for jsonObj in f:
                tweetDict = json.loads(jsonObj)
                listoftweets.append(tweetDict)
                for tweet in listoftweets:
                    if "text" in tweet:
                        thetext = tweet["text"]
                        thedate = tweet["created_at"]
                        preprocessed_text = preprocessing.preprocess_tweet(thetext)
                        new_row = {'created_at':thedate, 'text':thetext, 'preprocessed_text':preprocessed_text}
                        df = df.append(new_row, ignore_index=True)
        counter += 1
        if (counter > 100):
            break



    # ***Old code***                     
    # df = pd.DataFrame(columns=['created_at', 'text', 'preprocessed_text'])
    # rootdir = 'reorganized_data/cluster1'
    # counter = 0
    
    # for filename in os.listdir(rootdir):
    #     listoftweets = []
    #     with open(rootdir+"/"+filename, "r+") as f:
    #         for jsonObj in f:
    #             tweetDict = json.loads(jsonObj)
    #             listoftweets.append(tweetDict)
    #             for tweet in listoftweets:
    #                 if "text" in tweet:
    #                     thetext = tweet["text"]
    #                     thedate = tweet["created_at"]
    #                     preprocessed_text = preprocessing.preprocess_tweet(thetext)
    #                     new_row = {'created_at':thedate, 'text':thetext, 'preprocessed_text':preprocessed_text}
    #                     df = df.append(new_row, ignore_index=True)
        # counter += 1
        # if (counter > 100):
        #     break
                        
    df.to_csv("../../reorganized_data/cluster1/output.csv")
    print("Completed task.")
    
