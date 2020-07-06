import new_preprocessing

import os
import shutil

def move_data():
    file_list = new_preprocessing.get_data('../../../../data/twitterdata/')

    for x in range(16):
        dir_name = os.getcwd() + '/' + 'reorganized_data/' + 'cluster' + str(x + 1) + '/'

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)   
        
        for y in range(10000 * x, (10000 * x) + 10000):
            if y < len(file_list):
                shutil.copy(file_list[y], dir_name)              

if __name__ == "__main__":
    move_data()
