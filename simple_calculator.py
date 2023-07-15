# Simple Basic Calculator 
def add(p, q):
    return p + q


# subtraction

def subtraction(p, q):
    return p - q

# Multiplication

def multiplication(p, q):
    return p * q

# Division

try:
    def division(p, q):
        return p / q
except ZeroDivisionError as e:
    print(e)
while (True):
    print("Enter your choice ")
    print("a : For addition ")
    print("s : For substraction ")
    print("m : For multiplication ")
    print("d :For division")
    print("Enter zero for exit : ")
    choice = input("Enter your choice ")
    num_1 = int(input("Enter first number "))
    num_2 = int(input("Enter second number "))
    if choice == 'a':
        print(num_1, " + ", num_2, " = ", add(num_1, num_2))
    elif choice == 's':
        print(num_1, " - ", num_2, " = ", subtraction(num_1, num_2))
    elif choice == 'm':
        print(num_1, " * ", num_2, " = ", multiplication(num_1, num_2))
    elif choice == 'd':
        print(num_1, " / ", num_2, " = ", division(num_1, num_2))
    elif choice == "0":
        exit()
    else:
        print("Invalid choice ")
