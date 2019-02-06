import os
import json
import  time
from datetime import datetime, timedelta
import numpy as np

path = "/opt/data/twitter"
twitter_dir = os.listdir(path) # creates list object of all files in path

def init_time():
    file_path = path + "/" + twitter_dir[0]
    with open(file_path) as f:
        data = json.load(f)
        temp_time = datetime.strptime(
            data[0]['tweet_created'], "%Y-%m-%d %H:%M:%S"
        )
        return temp_time - timedelta(hours = 1) # sets time interval to 1 hour

earliest_time = init_time()
latest_time = init_time()
print("initial times:",earliest_time)

for i in range(0, len(twitter_dir)):
    file_path = path + "/" + str(twitter_dir[i])

    with open(file_path) as f:
        data = json.load(f)

        for j in range(0, len(data)):

            time1 = datetime.strptime(data[j]['tweet_created'], "%Y-%m-%d %H:%M:%S")

            if time1.date() < earliest_time:
                earliest_time = time1.date()
                print("New earliest_time:", earliest_time)
            elif time1.date() > latest_time:
                latest_time = time1.date()
                print("New latest_time:", latest_time)

out_file = open("times.txt","w")
out_file.write("earliest_time =",earliest_time)
out_file.write("latest_time =",latest_time)
out_file.close()
