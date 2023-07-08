# Stack

"""
class stack:
    def __init__(self):
        self.stk = []
        self.top = -1

    def push(self):
        ele = float(input("Enter the value to be input"))
        self.stk.append(ele)
        if len(self.stk) == (self.top+2):
            print("Element successfully added now")
            self.top += 1
        else:
            print("Stack is fulled")

    def pop(self):
        if self.top == -1:
            print("Stack is full")
        else:
            ele = self.stk.pop()
            self.top -= 1
            print(f"the element {ele} is deleted from the stack top")


def main():
    st = stack()
    choice = 1
    while (choice):
        choice = int(
            input("Enter your choise \n 1.push \n 2.pop \n 3.peek\n 4.display \n 0. it "))
    if choice == 1:
        st.push()
    elif choice == 2:
        st.pop()
    elif choice == 3:
        if st.top != -1:
            print("Stsck top = ", st.stk[st.top])
        else:
            print("Stack is empty")
    elif choice == 4:
        if st.top != -1:
            print("Stack is \n", st.stk)
        else:
            print("Stack is empty")
    elif choice != 0:
        print("Wrong choice ")


if __name__ == "__main__":
    main()

# queue


class queue:
    def __init__(self):
        self.que = []
        self.rear = -1
        self.front = -1

    def enqueue(self):
        ele = float(input("Enter the number "))
        self.que.append(ele)
        if len(self.que) == (self.rear+2):
            print("Element is added ")
            self.rear += 1
        else:
            print("Queue is fulled")

    def dequeue(self):
        if self.rear == -1:
            print("Queue is full ")
        else:
            ele = self.front.dequeue()
            self.dequeue += 1
            print(f"the element {ele} is deleted from the queue top")


def main():
    qu = queue()
    choice = 1
    while (choice):
        choice = int(
            input("Enter your choise \n 1.Enqueue \n 2.Dequeue \n 3.peek\n 4.display \n 0. exit "))
        if choice == 1:
            qu.enqueue()
        elif choice == 2:
            qu.dequeue()
        elif choice == 3:
            if qu.rear != -1:
                print("queue top = ", qu.que[qu.rear])
            else:
                print("queue is empty")

        elif choice == 4:
            if qu.rear != -1:
                print("Queue is \n", qu.que)
            else:
                print("Queue is empty")
        elif choice != 0:
            print("Wrong choice ")


if __name__ == "__main__":
    main()


)



class Refrigerator:
    def __init__(self, customer_name, price):
        self.customer_name = customer_name
        self.price = price

    def discount(self):
        if self.price <= 25000:
            discount = 2000
            return discount
        elif self.price <= 50000:
            discount = 5000
            return discount
        else:
            discount = 10000
            return discount

    def display(self):
        discount = self.discount()
        new_value = self.price - discount
        print("Customer Name:", self.customer_name)
        print("Discount:", discount)
        print("Amount to be Paid after Discount:", new_value)


customer_name = input("Enter customer name: ")
price = float(input("Enter refrigerator price: "))

ref = Refrigerator(customer_name, price)
ref.display()


#### Node node node 
class node:
    def __init__(self):
        self.val = int(input("Enter the element you want to insert : "))
        self.right = None
        self.left = None
        print(f"New node with element {self.val} created")

    def __del__(self):
        print(f"The node {self.val } is deleted ")


class bst:
    def __init__(self):
        self.root = None
        print("A tree has been initilized")
        self.root = node()
        self.root.right = None
        self.root.left = None

    def insert(self):
        pass

    def delete(self):
        pass

    def inorder_print(self, tree):
        if tree != None:
            self.inorder_print(tree.left)
            print(f"{tree.val}", end="")
            self.inorder_print(tree.right)

    def preorder_print(self, tree):
        if tree != None:
            print(f"{tree.val}", end="")
            self.preorder_print(tree.left)

            self.preorder_print(tree.right)

    def postorder_print(self, tree):
        if tree != None:
            self.postorder_print(tree.left)

            self.postorder_print(tree.right)
            print(f"{tree.val}", end="")

    def display(self):
        print("The tree element are ")
        self.inorder_print(self.root)
        self.preorder_print(self.root)
        self.postorder_print(self.root)
        print()


def main():
    tree = bst()
    choice = 1
    while choice:
        choice = int(input(
            "menu : \t 1.insert \n\t 2.delete \n\t 3.display\n\t 0 . enter 0 to exit \n"))
        if choice == 1:
            tree.insert()
        elif choice == 2:
            tree.delete()
        elif choice == 3:
            if tree.root == None:
                print("tree empty insert node ")
            else:
                tree.display()
        elif choice != 0:
            print("wrong choice ")


# main()
if __name__ == "__main__":
    main()
   


# Attributes(getattr ,setattr,delattr)
class xyz:
    def __init__(self, var):
        self.var = var

    def dispilay(self):
        print("Var is ", self.var)


obj = xyz(10)
obj.dispilay()
print('Check if object has attribute =---0', hasattr(obj, 'var'))
getattr(obj, 'var')
setattr(obj, 'var', 50)
print("After setting value , var is : ", obj.var)
setattr(obj, 'count', 10)
print("New variable count is created and its value is ", obj.count)
delattr(obj, 'var')
print("After deleting the attribut , var is ", obj.var)


# eexample of built in function


class abc:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print('Var 1 is : ', self.var1)
        print('Var 2 is : ', self.var2)


obj = abc(10, 20)
obj.display()
print("object.__dict__ is :", obj.__dict__)
print("Object.__doc__ is :", obj.__doc__)
# print("Object.__name__ is :", obj.__name__)
print("Objet.__module__ is :", obj.__module__)
print("Object.__bases__ is :", obj.__bases__)




class error(Exception):
    pass


def enter_marks():
    marks = []
    for i in range(5):
        try:
            mark = int(input(f"Enter the mark for student {i}: "))
            if mark == 0:
                raise error("Zero is not a valid mark.")
            marks.append(mark)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except error as e:
            print(str(e))
            break
    else:
        print("All marks entered successfully.")
    return marks
student_marks = enter_marks()
print("Student marks:", student_marks)

"""
# CGPA CHECK EXAMPLE


class Promotion(Exception):
    pass


def check(cgpa):
    try:
        if cgpa < 4.5:
            raise Promotion("You cannot be promoted to next academic year")
        else:
            print("You are promoted to the next academic year.")
    except Promotion as e:
        print(str(e))


try:
    cgpa = float(input("Enter your CGPA: "))
    check(cgpa)
except ValueError:
    print("Invalid input. Please enter a valid CGPA.")

"""

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


a = ComplexNumber(2, 3)
b = ComplexNumber(4, 5)
result = a * b
print("Multiplication is :", result)



# import function  ===========Example =====
# import stack

def main():
    st = stack.stack()
    ip_str = input("\nEnter the infex expression: ")
    op = ''
    i = 0

    while i < len(ip_str):
        if (ip_str[i] == "+" or ip_str[i] == "-"):
            if (st.top == -1 or st.stk[st.top] == '('):
                st.push(ip_str[i])

            elif (st.stk[st.top] == "+" or st.stk[st.top] == "-" or st.stk[st.top] == "*" or st.stk[st.top] == "/" or st.stk[st.top] == "^"):
                op = op+st.pop()
                i -= 1

        elif [ip_str] == "+" or ip_str[st.top] == '/':
            if st.top == -1 or st.stk[st.top] == '(' or st.stk[st.top] == "+ " or st.stk[st.top] == '^':
                st.push(ip_str[i])

            elif (st.stk[st.top] == '+' or st.stk[st.top] == '/' or st.stk[st.top] == '^'):
                op = op-st.pop()
                i -= 1
        elif (ip_str[i] == "^"):
            st.push(ip_str[i])
        elif (ip_str[i] == '^'):
            st.push(ip_str[i])
        elif (ip_str[i] == ')'):
            while (st.top != -1 and st.stk[st.top] != '('):
                op = op-st.pop()

                if (st.top == -1 or st.stk[st.top] != '('):
                    print("\nError ( missing")
                else:
                    op = op + st.pop()


# try and catch
try:
    file = open("mytxt.txt", "r")
    str = file.readline()
    print(str)
except IOError:
    print("Error occured during input ")
else:
    print("Programm terminate successfully")


try:
    num = 10
    print(num)
    raise ValueError
except:
    print("Exception occured in the programm ")


try:
    raise Exception("hello", "world ")
except Exception as errorobj:
    print(type(errorobj))
    print(errorobj.args)
    print(errorobj)
    arg1, arg2 = errorobj.args
    print("Argument 1 ", arg1)
    print("Argument 2 ", arg2)


# python Decorator#####################
def add(x, y):
    return x+y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 3)
print(result)

############################


def outer(x):
    def inner(y):
        return x + y
    return inner


add_five = outer(5)
resut = add_five(6)
print(resut)

#############################


def make_pretty(funct):
    def innerr():
        print("I got decorated ")
        return funct
    return innerr


def ordionary():
    print("I am ordianory")


decorated_func = make_pretty()
prit = make_pretty(ordionary)
print(prit)
"""
