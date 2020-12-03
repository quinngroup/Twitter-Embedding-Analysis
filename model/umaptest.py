import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})

#penguins = pd.read_csv("https://github.com/allisonhorst/palmerpenguins/raw/5b5891f01b52ae26ad8cb9755ec93672f49328a8/data/penguins_size.csv")
#penguins.head()

#penguins = penguins.dropna()
#penguins.species_short.value_counts()

#sns.pairplot(penguins, hue='species_short')


df = pd.read_csv("../../reorganized_data/cluster1/filled_matrix.csv")

print(df)

