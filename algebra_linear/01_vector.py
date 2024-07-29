from functools import reduce
import math

list1 = [1, 2, 3]
list2 = [2, 6, 7]
value = 3
vectors = [[1, 2 ,3], [4, 6, 7], [5, 7, 8]]

# somando vetores
def vector_add(v, w):
    # soma de elementos corrrespondentes
    # para subtrair, é só colocar o "-"
    return[v_i + w_i
        for v_i, w_i in zip(v, w)]

# subtraido vetores
def vector_subtract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

"""def vector_sum(vectors):
    result = vectors[0]value = 3
vectors = [[1, 2 ,3], [4, 6, 7], [5, 7, 8]]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result"""
def vector_sum(vectors):
    return reduce(vector_add, vectors)

# multiplicando vetores
def scalar_multiply(c, v):
    return[c * v_i for v_i in v]

# calculando a média do vetor
def vector_mean(vectors):
    n = len(vectors)
    print(1/n)
    print(vector_sum(vectors))
    return scalar_multiply(1/n, vector_sum(vectors))

# produto escalar
def dot(v, w):
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

# doma dos quadrados de um vetor
def sum_of_squares(v):
    return dot(v, v)

# magnitude ou tamanho de um vetor
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# distência entre dois vetores
def squared_distance(v, w):
    print(sum_of_squares(vector_subtract(v, w)))
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

# distência entre dois valores
def distance_02(v, w):
    return magnitude(vector_subtract(v, w))

print(distance_02(list1, list2))