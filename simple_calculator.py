# addition


def add(p, q):
    return p + q


# subtraction


def subtraction(p, q):
    return p - q


# Multiplication


def multiplication(p, q):
    return p * q


# Division


def division(p, q):
    return p / q


print("Enter your choice ")
print("a : for addition ")
print("s : for substraction ")
print("m : for multiplication ")
print("d :for division")
num_1 = int(input("Enter first number "))
choice = input("Enter your choice ")
num_2 = int(input("Enter second number "))
if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))
elif choice == 's':
    print(num_1, " - ", num_2, " = ", subtraction(num_1, num_2))
elif choice == 'm':
    print(num_1, " * ", num_2, " = ", multiplication(num_1, num_2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", division(num_1, num_2))
else:
    print("Invalid choice ")
