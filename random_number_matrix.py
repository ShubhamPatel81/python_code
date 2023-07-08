import numpy as np
# import random
# wap to formulate a matrix n * 2 using numpy random generation , each number is a floating point number , choose two random row vector . Find the similirty b/w the chossen sample and rest of the sample . and state which chossen to based on the row number and


def calculate_similarity(matrix, row1, row2):
    similarity = np.dot(matrix[row1], matrix[row2]) /\
        (np.linalg.norm(matrix[row1]) * np.linalg.norm(matrix[row2]))
    return similarity


def generate_similarity_matrix(n):
    matrix = np.random.rand(n + 2, n)
    row1, row2 = np.random.choice(n + 2, 2, replace=False)
    similarities = [
        calculate_similarity(matrix, row1, i) for i in range(n + 2) if i != row1
    ]
    similarities.extend(
        [calculate_similarity(matrix, row2, i) for i in range(n + 2) if i != row2])
    return matrix, similarities


n = 5
matrix, similarities = generate_similarity_matrix(n)
print("Matrix:")
print(matrix)
print("Similarities:")
print(similarities)
