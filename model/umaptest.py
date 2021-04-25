import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("../../reorganized_data/cluster1/filled_matrix.csv")

print(df)

