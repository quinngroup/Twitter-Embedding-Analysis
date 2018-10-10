import json, os
import pandas as pd
from pandas.io.json import json_normalize

def parse(file_name):
	with open("../twitter/" + file_name) as f:
		d = json.load(f)
		tweets = json_normalize(d)
		final = pd.DataFrame(tweets)
		return final

if __name__ == "__main__":
	for file in os.listdir('../twitter'):
		filename_w_ext = os.path.basename(file)
		# print(filename_w_ext)	
		filename, file_ext = os.path.splitext(filename_w_ext)	
		parse(file).to_csv(filename+".csv")
		
