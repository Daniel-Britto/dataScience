import pandas as pd
import numpy as np

notas = pd.Series([2, 7, 5, 10, 6], index=['Daniel', 'Renato', 'Maria', 'Pedro', 'Caio'])

print(notas)
print('Média: ', notas.mean())
print("Desvio padrão: ", notas.std())
print(notas.describe())
print(np.log(notas))