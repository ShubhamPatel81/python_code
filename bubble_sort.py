# # Bubblle sort
size = int(input("Enter the size of the list : "))
a = []
for i in range(size):
    val = int(input("Enter the value : "))
    a.append(val)
for j in range(1, size):
    temp = a[i]
    j = i - 1
while j >= 0 and temp < a[j]:
    a[j + 1] = a[j]
    j = j - 1
    a[j + 1] = temp

    print("Sorted element is :", a)

# ///////////////////////////////////////
