def max_ele(y, size, k):
    list.sort()
    return [len(list)-k]


# Finding the maximum Kth element of an array
# input the size of the array
size = int(input("Enter the size of the array : "))
list = []
# input the element of the array
for i in range(size):
    ele = int(input("Enter the element of the array : "))
    list.append(ele)
print(list)
y = len(list)
k = int(input("Enter the position to find max "))
x = max_ele(y, size, k)
print(x)
"""
# Printing the element of the array
for i in range(size):
    print(list[i])
list.sort(reverse=True)
print("Reverse of the array is : ")
print(list)
k = int(input("Enter the position to find the maximum element : "))
for i in range(size):
    max = list[size-k]

print(list)
"""
