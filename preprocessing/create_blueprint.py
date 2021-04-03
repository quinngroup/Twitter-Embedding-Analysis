import pandas as pd
import numpy as np

vocab_dict = pd.read_csv("../global_vocab.csv")
words = vocab_dict["word_set"].tolist()
# print(words[:5])
#print(words)

# print(vocab_dict[:5])

empty_mat = pd.DataFrame(np.zeros(shape=(len(words),len(words))))
empty_mat.columns = words
#print(empty_mat)
empty_mat = pd.concat([empty_mat, vocab_dict["word_set"]], axis=1)
#print(empty_mat)
empty_mat = empty_mat.set_index("word_set")
#print(empty_mat)
#print(empty_mat.columns.values)
empty_mat.to_csv("../empty_matrix.csv")


mat = pd.read_csv("../empty_matrix.csv", index_col="word_set")
#print(mat)
