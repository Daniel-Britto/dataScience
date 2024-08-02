import pandas as pd
import numpy as np

df = pd.read_csv('diamonds.csv')


maior_prec = max(df['price'])
menor_prec = min(df['price'])



print('------------------------INFORMAÇÕES----------------------------')
print(df.info())
print('-----------------------PRIMEIROS ITENS----------------------------')
print(df.head())
print('---------------------------CORTES E PREÇOS--------------------------')
print(df[['cut', 'price']])
print('---------------------------MENOR E MAIOR PREÇO--------------------------')
print('Maior valor: ', maior_prec)
print('Menor valor: ', menor_prec)
print('------------------MAIS BARATO-----------------------')
print(df[df.price == 326])
print('-------------------MAIS CARO---------------------------')
print(df[df.price == 18823])
print('---------------------MÉDIA E MEDIANA DO PREÇO---------------------------')
print('Média: ', np.mean(df.price))
print('Mediana: ', np.median(df.price))
print('-------------------PRECENTILES---------------------------')
print("Precentil de 50%: ", np.percentile(df.price, 91))

