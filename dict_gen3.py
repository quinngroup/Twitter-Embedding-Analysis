# latest_time: 2018-09-20 17:24:35
# earliest_time: 2018-01-22 20:55:01
# 30 weeks - 30 time files

import os
import json
import  time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# opens twitter directory
path = "/opt/data/twitter"
twitter_dir = os.listdir(path) # creates list object of all files in path

# gets the file time of a current file for comparison with checkpoint time
def file_time(file_ind, data_ind):
    file_path = path + "/" + twitter_dir[ind[file_ind]]
    with open(file_path) as f:
        data = json.load(f)
        temp_time = datetime.strptime(
            data[data_ind]['tweet_created'], "%Y-%m-%d %H:%M:%S"
        )
        return temp_time

# start and end times
start_time = datetime.datetime(2018,1,22,20,55,1)
end_time = datetime.datetime(2018,1,29,20,55,1)

print(star_time.strftime("%Y-%m-%d %H:%M:%S"))
print(star_time.strftime("%Y-%m-%d %H:%M:%S"))

output_file = open("../dicts/2018-01-22.txt", 'w') # file to save first time seg
print("opened: ", output_file.name) # error checking

for i in range(0, len(twitter_dir)):   # iterates through all files
    for j in range(0, len(data)):   # iterates through all data in a file
        # if checkpoint is less then the file time its time for a new time interval
        # seems like tweets are appended to the top of a file
        if star_time < file_time(i, j) and end_time > file_time(i,j):
            print("writing tweet from time:",file_time(i,j))
            output_file.write(data[j]['tweet_text']) # writes the tweet to file

output_file.close()
