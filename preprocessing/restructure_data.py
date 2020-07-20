import new_preprocessing
import preprocessing

import os
import shutil
import pandas as pd
from pandas import DataFrame
import json
import gzip

def move_data():
    
    '''This function seperates our Twitter Data (originally in a single directory of 157345
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

def make_giant_json(cluster_directory_path):

    '''Creates a giant .json file.

    Key-arguments: cluster_directory_path - the relative path to the cluster directory
    e.g. ../../reorganized_data/cluster1

    Returns: A dataframe of unprocessed data

    '''
    current_json_dict = dict()

    file_list = new_preprocessing.get_data(cluster_directory_path)

    for current_file in file_list:
        with gzip.GzipFile(current_file, 'r') as fil:
            data_bytes = fil.read()
            data = json.loads(data_bytes.decode('utf-8'))
            data.update(current_json_dictionary)
            fil.seek(0)
            json.dump(data, fil)

    return pd.DataFrame.from_dict(current_json_dict)

def convert_to_csv(cluster_directory_path):

    '''Converts all of the .json files in a cluster directory into a csv file.
    This happens in the steps, creating a giant dictionary  -> unprocessed df ->
    processed df -> csv.

    Key-arguments: cluster_directory_path - the relative path to the cluster directory
    e.g. ../../reorganized_data/cluster1

    Output: a single .csv file found in the directory path this function was given a reference to.
    '''

    new_preprocessing.get_data('../../reorganized_data/cluster1')
    
    
    # Get all of the files in a cluster directory path
    # Add them to a panda df
    # `pd_df.to_csv(r'cluster_directory_path', index = False, header =True)`


if __name__ == "__main__":
    make_giant_json('../../reorganized_data/cluster1/')
