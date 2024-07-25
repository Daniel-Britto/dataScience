import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# valores unicos na coluna
print(df['bairro'].unique())
# hegemoneidade da amosta
print(df['bairro'].value_counts(normalize=True)*100)
# agrupando dados se basendo em critérios
print(df.groupby('bairro').mean())
# extraindo dados de uma coluna por metro quadrado
print(df.groupby('bairro').mean()['pm2'].sort_values())
# reduzindo nomes
def truncar(bairro):
    return bairro[:3]
print(df['bairro'].apply(truncar))

# NaN
df2 = df.head()
df2 = df2.replace({'pm2': {12031.25: np.nan}})
print(df2)
# prenchendo valores NaN
print(df2.fillna(99))
# removendo linhas Nan
#print(df2.dropna())
# descobrindo valores NaN
print(df2.isna())
