#!/usr/bin/env python

import os
import gensim
from gensim import corpora
from gensim.models import LdaModel, LdaMulticore
from gensim.utils import simple_preprocess, lemmatize
from nltk.corpus import stopwords
import re
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.root.setLevel(level=logging.INFO)
stop_words = stopwords.words('english')
stop_words = stop_words + ['com', 'edu', 'subject', 'lines', 'organization', 'would', 'article', 'could']

docs = open('dicts/03:50:14.txt','r')
data = [[text for text in doc.split()] for doc in docs]


data_processed = []

for i, doc in enumerate(data[:100]):
  doc_out = []
  for wd in doc:
    if wd not in stop_words:
        doc_out.append(wd)
    else:
        continue

  data_processed.append(doc_out)

docs.close()

print(data_processed[0][:5])

dct = corpora.Dictionary(data_processed)
corpus = [dct.doc2bow(line) for line in data_processed]

lda_model = LdaMulticore(corpus=corpus, id2word=dct, random_state=100, num_topics=7, passes=10, chunksize=1000,
                         batch=False, alpha='asymmetric', decay=0.5, offset=64, eta=None, eval_every=0, 
                         iterations=100, gamma_threshold=0.001, per_word_topics=True)

lda_model.save('doc1.model')

# lda_model.print_topics(-1)

for c in lda_model[corpus[5:8]]:
  print("Document Topics      : ", c[0])
  print("Word id, Topics      : ", c[1][:3])
  print("Phi Values (word id) : ", c[2][:2])
  print("Word, Topics         : ", [(dct[wd], topic) for wd, topic in c[1][:2]])
  print("Phi Values (word)    : ", [(dct[wd], topic) for wd, topic in c[2][:2]])
  print("--------------------------------------------------\n")
