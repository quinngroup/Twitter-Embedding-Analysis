import pandas as pd
import numpy as np
import wordcloud

df = pd.read_csv("../../reorganized_data/cluster1/vocab_dict.csv")
df.columns=["word","count"]

vocab = df["word"].tolist()

wc = wordcloud.WordCloud.generate(vocab)

wc.to_file("wordcloud1.png")
