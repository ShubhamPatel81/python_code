# Sparcing of matrix is to take out all the position and value of the row and column in a matrix
from multiprocessing import Value
from optparse import Values

print("hello world ")
"""

def sparse(matrix):
  dist = {}
  for row, i in enumerate(matrix):
    for col, j in enumerate(i):
      if Values != 0:
        dist[(i, j)] = Value
  return sparse


print(sparse)

matrix = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
printmat = sparse(matrix)
print(printmat)
# sparse_matrix_dictionary = {(0,1):1, (1,1):1}
"""


def matrix_to_sparse_dict(matrix):
    sparse_matrix_dict = {}
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value != 0:
                sparse_matrix_dict[(row_idx, col_idx)] = value
    return sparse_matrix_dict


# Example usage:
matrix = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
sparse_matrix_dictionary = matrix_to_sparse_dict(matrix)
print(sparse_matrix_dictionary)
