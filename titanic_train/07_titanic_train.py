import pandas as pd
from matplotlib import pyplot as plt

base = pd.read_csv('titanic_train.csv')

# gráfico de linha
plt.title('Valores por Classe')
plt.ylabel('Taxas')
plt.xlabel('Classes')
plt.bar(base.Pclass, base.Fare)
plt.show()


# 5 primeiras linhas
print(base.head())

# 5 últimas linhas
print('---------------------------------------------------------------')
print(base.head())

# tamnho da base
print('---------------------------------------------------------------')
print(base.shape)

# nome das colunas
print('---------------------------------------------------------------')
for col in base.columns:
    print(col)

# tudo de uma vez
print('---------------------------------------------------------------')
print(base)

# observando os tipos de dados
print('---------------------------------------------------------------')
print(base.dtypes)

# mostrando tipos de dados e valores vazios
print('---------------------------------------------------------------')
print(base.info())

# contando valores vazios por coluna
print('---------------------------------------------------------------')
print(base.isnull().sum())

# resumo estatístico
print('---------------------------------------------------------------')
print(base.describe())

# buscando por coluna
print('---------------------------------------------------------------')
print(base['Survived'])

# quantidade de vezes que o valor aparece na coluna
print('---------------------------------------------------------------')
print(base.Survived.value_counts())

# selecionando conjunto de colunas
print('---------------------------------------------------------------')
print(base[['PassengerId', 'Survived', 'Fare']])

# verificando clientes qeu pagam mais de 100 libras
print('---------------------------------------------------------------')
print(base[base.Fare > 500])

# verificando clintes que pagaram menos de 5 libras
print('---------------------------------------------------------------')
print(base[base.Fare < 5])

# verificando se alguém viajou com esposa e filhos
print('---------------------------------------------------------------')
print(base[(base.Parch > 1) & (base.SibSp < 1)].head())


# procurando linhas e colunas específicas
print('---------------------------------------------------------------')
print(base.iloc[30:40, 3:6])

# procurando coluna Pclass and Fare
print('---------------------------------------------------------------')
print(base.Pclass, base[base.Fare > 400])