import os
import json
import  time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# open twitter directory
path = "/opt/data/twitter"
twitter_dir = os.listdir(path)

# finds order of file sby time
dir = np.array(twitter_dir)
ind = dir.argsort()


# this gets the first time and creates a time variable 
# that is 12 hours in the future so the file
# knows when to make a new file
def init_time():
  time1 = datetime.now()
  file_path = path + "/" + twitter_dir[ind[0]]
  with open(file_path) as f:
    data = json.load(f)
    temp_time = datetime.strptime(data[0]['tweet_created'], "%Y-%m-%d %H:%M:%S")
    return temp_time + timedelta(hours=12)

def file_time(cur_file, cur_ind):
  time1 = datetime.now()
  file_path = path + "/" + twitter_dir[ind[cur_file]]
  with open(file_path) as f:
    data = json.load(f)
    temp_time = datetime.strptime(data[cur_ind]['tweet_created'], "%Y-%m-%d %H:%M:%S")
    return temp_time

# tester method
def tester():
  print("started")
  print("init_time: 2018-04-06 21:39:38")
  print(init_time())
  print("file_time: 2018-08-05 00:31:47")
  print(file_time(3,87))

def main():
  comp_time = init_time()  # created first time interval

  name = str(comp_time)
  f = open("dicts/" + name + ".txt", "w+")

  for file in twitter_dir:  # goes through all the files in twitter dir
    for i in range(0, len(ind)):   # iterates through ind so files will be check in correct order

      pt = path + "/" + str(twitter_dir[ind[i]])   # gets path for the file
      with open(pt) as d:        # open the f#ilpaces after keyword

        acc_d = json.load(d)            # loads in the json info from file
        for j in range(0, len(acc_d)):    # allows us to go  through all the elements in the json

          if comp_time.date() < file_time(i,j).date():    # checks to see if new time file needs to be created
            i =  file_time(i,j) + timedelta(hours=12)    #   updates time if time is past 12 hours
            # make a newtext file and write to that one
            print("closing " + name)
            f.close()   # closes f so we can change it to the new file
            name = str(file_time(i,j)) + ".txt"   # creates new name for file out of its time combination of a date and a time.

            f = open("dicts/" + name, "w")         # sets f to be the new file
            f.write(acc_d[j]['tweet_text']) # writes the tweets to the text
          f.write(acc_d[j]['tweet_text']) # writes the tweets to the text


if __name__ == "__main__":
  tester()
  main()
