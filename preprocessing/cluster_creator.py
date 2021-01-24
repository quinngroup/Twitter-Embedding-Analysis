import os
import datetime
import pandas as pd
from shutil import copyfile

NUM_CLUSTERS = 18

def find_end_date(start_date):
  start_month = start_date.month
  if start_month == 1 or start_month == 2:
    end_date = start_date + datetime.timedelta(days=59)
  elif start_month >= 3 and start_month <= 6:
    end_date = start_date + datetime.timedelta(days=61)
  elif start_month >= 8 and start_month <= 11:
    end_date = start_date + datetime.timedelta(days=61)
  else:
    end_date = start_date + datetime.timedelta(days=62)
  return end_date

def create_dirs():
  for i in range(NUM_CLUSTERS):
    dir_name = os.mkdir("../reorganized_data/cluster"+str(i))

# read in file names from raw data
path_to_raw = "/opt/data/twitter/data/twitterdata"
data_files = os.listdir(path_to_raw)

# parse file names for date
fname_w_time = {}
time_w_fname = {}
for f in data_files:
  time_str = f[29:39]
  if time_str == "":
    continue
  datetime_time = datetime.datetime.strptime(time_str, '%Y_%m_%d')
  #print(f, time_str, datetime_time)
  fname_w_time[f]= datetime_time
  time_w_fname[datetime_time] = f

df_fname_w_time = pd.DataFrame.from_dict(fname_w_time, orient='index',columns=['date']) # convert dictionary to dataframe
df_fname_w_time["date"] = pd.to_datetime(df_fname_w_time["date"]) # makes sure the dates are a datetime object 

print(len(data_files))
print(len(fname_w_time))

# find out how many cluster are wanted from command line input
# by default 18 clusters of 2 month segments are created
create_dirs()
start_date = datetime.datetime.strptime("2014-01-01", '%Y-%m-%d')
end_date = find_end_date(start_date)

#print(df_fname_w_time[:10])

for i in range(NUM_CLUSTERS):
  clust_path = "../reorganized_data/cluster"+str(i)
  print("creating cluster", i)
  print(start_date, end_date)
  temp_df = df_fname_w_time[df_fname_w_time["date"].between(start_date, end_date)]
  cluster_fnames = temp_df.index
  for f in cluster_fnames:
    copyfile(path_to_raw+"/"+f,clust_path+"/"+f)


  start_date = end_date + datetime.timedelta(days=1)
  end_date = find_end_date(start_date)

# create reoganized data folder in parent folder
#
# move correct files to correct cluster
# 
