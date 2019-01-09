#!/usr/bin/env python

# imports
import os
import re
import numpy as np
from datetime import datetime, timedelta
import json

print("test")
# lists a directory
def load_dir(file_path):
    return os.listdir(file_path)

# returns a list that represents the files in order of creation
def get_ind(dir):
    arr = np.array(dir)
    return arr.argsort()

# returns number of elements in a file
def get_len(file_path):
    with open(file_path) as f:
        data = json.load(f)
        return len(data)

# returns the time the tweet was tweeted
def tweet_time(ind, file_path):
    with open(file_path) as f:
        data = json.load(f)
        return datetime.strptime(data[ind]['tweet_created'], "%Y-%m-%d %H:%M:%S")

def get_tweet(ind, file_path):
    with open(file_path) as f:
        data = json.load(f)
        return data[ind]['tweet_text']

def write_txt(cur_file_time, i):
    if os.path.exists("dicts/" + cur_file_time.strftime("%H:%M:%S") + ".txt"):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    f = open("dicts/" + cur_file_time.strftime("%H:%M:%S") + ".txt", append_write)

    tweet = get_tweet(i, "twitter/tweets1.json")
    tweet = tweet.replace('RT', '')
    tweet = tweet.replace(',', '')
    tweet = tweet + ","
    tweet = tweet.replace("\n", ' ')
    tweet = filter(lambda x:x[0]!='@', tweet.split())

    for word in tweet:
        f.write(word + " ")
    f.write("\n")
    f.close()


def main():
    print("start ")
    twitter_dir = load_dir("twitter")
    ind = get_ind(twitter_dir)

    # sets initial time point for comparison
    cur_file_time = tweet_time(get_len("twitter/tweets1.json")-1, "twitter/tweets1.json") + timedelta(hours=6)
    print("Initial file time", cur_file_time)
    write_txt(cur_file_time, 0)

    for elem in twitter_dir:
        for j in range(0, len(ind)):
            path = "twitter/" + twitter_dir[ind[j]]
            with open(path) as d:
                i = get_len(path) - 2
                while not i == 0:
                    file_time = tweet_time(i, path)
                    if cur_file_time < file_time:
                        print("Created new file", file_time)
                        cur_file_time = file_time + timedelta(hours=6)
                        write_txt(cur_file_time, i)
                    else:
                        write_txt(cur_file_time, i)
                    i = i - 1

main()
print("done")
