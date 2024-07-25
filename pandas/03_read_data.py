import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# exibe as primeiras linhas
print(df.head(n=10))
#exibe as últimas linhas
print(df.tail())