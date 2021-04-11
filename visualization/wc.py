import pandas as pd
import numpy as np
from wordcloud import WordCloud

df = pd.read_csv("../../reorganized_data/cluster0/vocab_dict.csv").dropna()
df.columns=["word","count"]

vocab = df["word"].tolist()
print(len(vocab))
vocab = ".".join(vocab)
#print(vocab)
wc = WordCloud().generate(vocab)

wc.to_file("wordcloud0.png")
