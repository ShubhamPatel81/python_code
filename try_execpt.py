# If the block of code is correct then try block will be execute else except block is executed

try:
    print("Enter the number :")
    marks = int(input())
    if marks < 0 or marks > 100:
        raise ValueError
    print("Marks is : ", marks)
except ValueError:
    print("Input out of range ")
