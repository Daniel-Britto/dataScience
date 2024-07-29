A = [[1, 2, 3], 
    [4, 5, 6]]

B = [[1, 2],
    [3, 4],
    [5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]

# criando matrizes
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
             for j in range(num_cols)]
             for i in range(num_rows)]

# matriz de identidade
def is_diagonal(i, j):
    return 1 if i == j else 0

i = []
j = []

print(make_matrix(3, 3, (A, B)))