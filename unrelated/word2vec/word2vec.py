from preproc import tokenize
from skip import word2vec
import pandas as pd 

settings = {
	'window_size': 2,	# context window +- center word
	'n': 10,		# dimensions of word embeddings, also refer to size of hidden layer
	'epochs': 50,		# number of training epochs
	'learning_rate': 0.01	# learning rate
}

raw_tweet_data = pd.read_csv('twitter-dataset-avengersendgame/tweets.csv', encoding='cp1252', index_col=0)

raw_text = raw_tweet_data['text']
corpus = []
for tweet in raw_text:
    corpus.append(tokenize(tweet))

w2v = word2vec()
training_data = w2v.generate_training_data(settings, corpus)
