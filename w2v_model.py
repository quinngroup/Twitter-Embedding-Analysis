#!/usr/bin/env python

from gensim.models.word2vec import Word2Vec
from gensim import corpora
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

docs = open('dicts/03:50:14.txt','r')
data = [[text.lower() for text in doc.split()] for doc in docs]


model = Word2Vec(data, min_count=0, workers=10)
model.save('corp/w2vdoc1')
print(model.most_similar("safe"))
