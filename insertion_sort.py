'''
def InsertionSort(a):

 # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
        temp = a[i]

# Shift elements of array[0 to i-1], that are greater than temp, to one position ahead of their current position
    for j in range(i):
        if j < a[j]:
           a = a[:j]+[temp]+a[j:]
           break

    temp = a[j]
    a[j] = a[j+1]
    a[j+1] = temp
    j = i-1
    while j >= 0 and temp < a[j]:
        a[j+1] = a[j]
        j = j - 1
        a[j+1] = temp


# # # array to be sorted
a = [10, 5, 13, 8, 2]
InsertionSort(a)
print("Array after sorting:")
print(a)

'''


# ///////////////////////////////////////
# Insertion sort using recursion sort
def recursive_insertion_sort(arr, n):
    # Base case: if the array has only one element, it is already sorted
    if n <= 1:
        return

    # Sort the first n-1 elements recursively
    recursive_insertion_sort(arr, n - 1)

    # Insert the nth element in its correct position
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
recursive_insertion_sort(arr, len(arr))
print(arr)
