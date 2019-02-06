import os
import json
import  time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# opens twitter directory
path = "/opt/data/twitter"
twitter_dir = os.listdir(path) # creates list object of all files in path

#print(twitter_dir)

# find order of file by time created
dir = np.array(twitter_dir)
ind = dir.argsort()

print("dir",dir)
print("ind",ind)

# this gets the first time and creates a time variable
# and adds 1 hours to the time since we want to be able to
# check once the 1 hour mark is passed so we can create
# a new file
def init_time():
    file_path = path + "/" + twitter_dir[ind[0]]
    with open(file_path) as f:
        data = json.load(f)
        temp_time = datetime.strptime(
            data[0]['tweet_created'], "%Y-%m-%d %H:%M:%S"
        )
        return temp_time - timedelta(hours = 1) # sets time interval to 1 hour

# gets the file time of a current file for comparison with checkpoint time
def file_time(file_ind, data_ind):
    file_path = path + "/" + twitter_dir[ind[file_ind]]
    with open(file_path) as f:
        data = json.load(f)
        temp_time = datetime.strptime(
            data[data_ind]['tweet_created'], "%Y-%m-%d %H:%M:%S"
        )
        return temp_time

def main():
    comp_time = init_time() # gets initial time of first tweet

    file_name_inc = 0
    output_file = open("../dicts/time" + str(file_name_inc) + ".txt", 'w') # file to save first time seg
    print("opened: ", output_file.name) # error checking

    for i in range(0, len(ind)):   # iterates through all files
        file_path = path + "/" + str(twitter_dir[ind[i]])

        with open(file_path) as f:
            data = json.load(f)

            for j in range(0, len(data)):   # iterates through all data in a file
                # if checkpoint is less then the file time its time for a new time interval
                # seems like tweets are appended to the top of a file 
                if comp_time.date() > file_time(i, j).date():
                    print("time checkpoint reached.") # error checking

                    output_file.close()

                    file_name_inc+=1
                    output_file = open("../dicts/time" + file_name_inc + ".txt", w)

                    output_file.write(data[j]['tweet_text']) # writes first tweet to file

                    comp_time = file_time(i,j) - timedelta(hours=1)
                else:
                    print("Current File Time:",file_time(i,j))
                    output_file.write(data[j]['tweet_text']) # writes the tweet to file

if __name__ == "__main__":
    main()
