
# Generate an numpy ndarray of size N*M called A. Here each element is a ϐloating point number between .0 and 1.0. Calculate the dot product between A and A-Transpose. Then write the code to validate whether the output matrix is a symetric matrix or not.


import numpy as np
matrix = np.random.rand(3, 4)
print("Original matrix :\n", matrix)
# Calculate the dot product between A and its transpose
dot_product = np.dot(matrix, matrix.transpose())
# Check if the resulting matrix is symmetric
symmetric = np.allclose(dot_product, dot_product.transpose())
print("Symmetric matrix : \n ", symmetric)
# Print the dot product matrix and whether it is symmetric or not
print("Dot product matrix:")
print(dot_product)
if symmetric:
    print("The dot product matrix is symmetric.")
else:
    print("The dot product matrix is not symmetric.")
