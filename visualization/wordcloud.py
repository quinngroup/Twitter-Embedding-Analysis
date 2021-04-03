import pandas as pd
import numpy as np
from wordcloud import WordCloud

df = pd.read_csv("../../reorganized_data/cluster1/vocab_dict.csv")
df.columns=["word","count"]

vocab = df["word"].tolist()

wc = WordCloud.generate(vocab)

wc.to_file("wordcloud1.png")
