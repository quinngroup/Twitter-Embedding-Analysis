import math
import pandas as pd
from scipy.sparse import csc_matrix, save_npz

wc = pd.read_csv("wc/wc0.csv")
wc.columns = ["words", "count"]
# wc = wc.rename(index=str, columns={"words": "count", "count": "words"})
print(wc.head())

wnd = pd.read_csv("wnd/wnd0.csv")
wnd.columns = ["word1", "word2", "count"]
# wnd = wnd.rename(columns={"word1": "word2", "word2":"word1"})
# print("\n")
print(wnd.head())

def sum_dict(df):
    # Finds the total word count
    sum = 0
    for i in range(len(df)):
      sum = sum + df["count"][i]
    return sum

def create_PMI(wc, wnd):
    """
    Creates PMI matrix based on inputed wc and wnd
    Parameters:
    wc - word count dataframe
    wnd - window count dataframe
    Output:
    A PMI matrix
    """
    len_d = sum_dict(wc)  # gets number of words
    PMI = csc_matrix((len(wnd["word2"]), len(wnd["word2"])), dtype=float)  # scipy sparse matrix
    
    x = 0
    y = 0
    for j in range(len(wnd["word2"])):
        for k in range(len(wnd["word2"])):
            word1 = wnd["word2"].iloc[j]
            word2 = wnd["word2"].iloc[k]
            try: 
                word1_count = wc[wc["words"] == word1]["counts"].item()
                word2_count = wc[wc["words"] == word2]["counts"].item()
                # print(word1_count, word2_count)
                # print("word1: " + str(word1),", word2: " + str(word2))
                df1 = wnd.loc[wnd.word1 == word1]
                df1 = df1.loc[df1["word2"] == word2]
                wnd_value_count = df1["count"].iloc[0]
                # print("wnd count: " + str(wnd_value_count))

                t = wnd_value_count * len_d
                b = word1_count * word2_count
                fin = math.log(t/b)
                PMI[x, y] = fin  # final value is added to PMI
                print("PMI[" + str(x) + ", " + str(y) + "] = " + str(fin))
                y = y + 1
            except KeyError:
                print("key Error")
        x = x + 1
        y = 0
    save_npz("../matrices/PMI0.npz", PMI)

create_PMI(wc, wnd)
