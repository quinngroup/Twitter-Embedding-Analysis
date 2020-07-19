import new_preprocessing

import os
import shutil


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

def convert_to_csv(cluster_directory_path):

     '''Converts all of the .json files in a cluster directory into a csv file.


     Output: a single .csv file found in the directory path this function was given a 
     reference to.

     '''

     # Get all of the files in a cluster directory path
     # Add them to a panda df
     # `pd_df.to_csv(r'cluster_directory_path', index = False, header =True)`


if __name__ == "__main__":
    move_data()
