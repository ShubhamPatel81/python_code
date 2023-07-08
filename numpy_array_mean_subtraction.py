# Generate an N*M matrix and store it in numpy ndarray. Find the column mean for each column.Then subtract the column means with its respective column elements. Print the resultant matrix.

import numpy as np
nums = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array elements:")
print(nums)
# Finding mean of the matrix of column
col_means = np.mean(nums, axis=0)
print("\nMean of each column :")
print(col_means)
# Subtract the mean of each column from each element
print("\nSubtract the mean of each column from each element:")
result = nums - col_means
print(result)
