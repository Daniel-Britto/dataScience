import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Aluno': ['Daniel', 'Maria', 'Pedro'],
    'Faltas': [3, 4, 6],
    'Prova': [2, 5, 7],
    'Seminário': [4.6, 7.8, 3.6]
})

print(df)
#tipos de dados
print(df.dtypes)
#lista de colunas
print(df.columns)
#valores das colunas
print(df['Prova'])
print(df.describe())
#ordenando por colunas
print(df.sort_values(by='Seminário'))
#selecionando o dado
print(df.loc[2])
#selecionando por condição
print(df[df['Seminário'] < 7.0])