num = int(input("Enter the number "))
num = num * 2 + 1
for i in range(num):
    for j in range(num):
        if (i == j and i < num / 2) or (i + j == num - 1 and i < num / 2):
            print("*", end="")
        else:
            print(" ", end=" ")
    print()

# printing star
i = 1
while (i <= 5):
    j = 1
    while (j <= i):
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1
print("\n")

# Example 2
i = 1
while (i <= 9):
    b = 1
    while (b <= 9 - i):
        print(" ", end=' ')
        b = b + 1

    j = 1
    while (j <= i):
        print("*", end=' ')
        j = j + 1
    print()
    i = i + 1
# pyramid
i = 1
k = 1
while (i <= 6):
    b = 1
    while (b <= 6 - i):
        print(" ", end=" ")
        b = b + 1

    j = 1
    while (j <= k):
        print("*", end=" ")
        j = j + 1
    k = k + 2
    print()
    i = i + 1

# Pyramid \
rows = int(input("Enter the rows"))
for i in range(rows):
    print(" " * (rows - i) + " *" * (i + 1))
for j in range(rows - 1):
    print(" " * (j + 2) + " *" * (rows - 1 - j))
