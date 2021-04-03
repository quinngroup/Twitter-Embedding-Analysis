import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("../../reorganized_data/cluster0/vocab_dict.csv").dropna()
df.columns = ["word","count"]

print(df[:5])

p = plt.bar(df["word"],df["count"])
plt.savefig("bar.png")
