import numpy
import pandas as pd
import gensim as gn
import json
import os

def format_file(file):
  stop_words = ["for", "a", "of", "the", "and", "to", "in", "rt", "is"]
  with open("../twitter/" + file) as json_open:
    dict = json.load(json_open)
    f = [dict[i]['tweet_text'].lower() for i in range(len(dict))]
    f2 = [row for rom in f]
    f3 = []
    for ent in f2:
      words = ent.split()
      for word in words:
        if word in stop_words:
          words.remove(word)
      f3.append(words)
  return f3

def gen_uniques(raw_dict):
  uniques = []
  for i in range(len(raw_dict)):
    for j in range(len(raw_dict[i])):
      if raw_dict[i][j] in uniques:
        continue
      else:
        uniques.append(raw_dict[i][j])
  return uniques

def save_fdata(data, file):
  f_bn = os.path.basename(file)
  f_name = os.path.splitext(f_bn)[0]
  f = open(f_name+".txt","w+")
  for i in range(len(data)):
    f.write(data[i]+'\n')
  f.close()

def_create_dicts(directory):
  for filename in os.listdir(directory):
    f = format_file(filename)
    uniques_f = gen_uniques(f)
    save_fdata(uniques_f, filename)

create_dicts("/opt/data/twitter")

