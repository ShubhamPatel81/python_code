size = int(input("Enter the size of the array : "))
list = []
print("Enter the element of the array/list")
for i in range(size):
    ele = int(input())
    list.append(ele)
print("Element of the array/list is : ")
for i in range(size):
    print(list[i])
"""

maximum = max(list)
print("Maximum number is : ", maximum)
minimum = min(list)
print("Minimum element is : ", minimum)
"""
for i in range(size):
    list.sort()
print(list)
print(f"{list[0]} is minimimum element ")

print(f"{list[size-1]} is maximum element ")
