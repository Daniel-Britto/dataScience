import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import math

num_friends = [100, 49, 41, 49, 25, 78, 4, 35, 56, 34, 28, 78, 22,98]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Histograma da Contagem de Amigos')
plt.xlabel('# de amigos')
plt.ylabel('# de pessoas')
#plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

# média
def mean(x):
    return sum(x) / len(x)

# mediana
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi] / 2)
    
# quantil
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


# moda (valores comuns)
def model(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

# ampitude medida de dispersão
def data_range(x):
    return max(x) - min(x)

# variância medida de dispersão
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def dot(v, w):
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
    
# desvio padrão
def standard_deviation(x):
    return math.sqrt(variance(x))

# percentos
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

daily_minutes = [22.45, 34, 67, 78, 45]

# covariânce
def covariance(x, y):
    n  = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)



print(num_points, largest_value, smallest_value)
print('Méia: ', mean(num_friends))
print('Mediana: ', median(num_friends))
print('Quartil: ', quantile(num_friends, 0.25))
print('Moda: ', model(num_friends))
print('Amplitude: ', data_range(num_friends))
print('Variância: ', variance(num_friends))
print('Desvio Padrão: ', standard_deviation(num_friends))
print('Quantile: ', interquartile_range(num_friends) )
print('Covariância: ', covariance(num_friends, daily_minutes))