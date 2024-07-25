import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

#df['preco'].plot.hist(bins=30, edgecolor='black')

#df['bairro'].value_counts().plot.bar()

#df['bairro'].value_counts().plot.barh(title='Número de apartamentos')

#plt.style.use('ggplot')
#df.plot.scatter(x='preco', y='area')

#df['quartos'].value_counts().plot.pie()

#df.plot.scatter(x='preco', y='area', s=.5)

df.sample(frac=.1).plot.scatter(x='preco', y='area')

plt.show()
