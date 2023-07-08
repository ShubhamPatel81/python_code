"""
message = "Hello!"
index = 0
for i in message:
    print("message [", index, "] = ", i)
    index = index + 1
str1 = "Hello "
str2 = "World!"
str3 = str1 + str2
print(str3)

str = "Hello "
print(str*4)

r1 = "Hello , "
me = input("Enter your name :")
r1 = str1+name
int(str1, " Welcome to Python Coading ")
name = "Shubham "
age = 18
print("Name = %s and Age = %d " % (name, age))
print("Name = %s and Age = %d " % ("Harry", 17))
print(name.center(12, '*'))
# print(ord(name))
strq = 'A'
print(ord(strq))
SA = 98
print(chr(SA))


mesages = " Welcome to the pyhton World "
index = 0
while index < len(mesages):
    letter = mesages[index]
    print(letter, end=' ')
    index = index + 1

# Enamurate function
mesages = " Welcome to the pyhton World "
for index, message in enumerate(mesages):
    print(message)
    if (index == 4):
        print("Good Job !")


a = 12
b = 23
print("A = ", a) if a > b else print("A = B") if a == b else print("B = ", b)

local and global variable \
x = 4
print(x)


def hello():
    x = 5
    y = 1
    print(f"The local variable x is {x} and y is {y}")


hello()
print("the global variable of x is {x} ")


#FILE HANDLING
f = open("myfile.txt", "r")
txt = f.read()
print(txt)
f.close()

f = open("myfile.txt", "w")
f.write("Hello!, Welcome to python world ")
f.close()

f = open("myfile.txt", "r")
t = f.read()
print(t)

f = open("myfile.txt", "a")
f.write("Python is a simple and easy language \n")
f.close()


# reading file
f = open("myfile.txt", "r")
while True:
line = f.readline()
print(line)
if not line:
break
print(line )
def matrix(mat, k):
row = len(mat)
col = len(mat[0])
for i in range(row):
for j in range(col):
mat[i][j] = mat[i][j]*k
return mat

mat = [[2, 3], [5, 4]]
k = 5
result = matrix(mat, k)
print(result)

def test_even_values(d):
result = {}
for key, values in d.items():
Check if all the values in the list are even
all_even = all(val % 2 == 0 for val in values)
result[key] = all_even

return result
d = {"Dic1": [6, 8, 10], "Dic2": [8, 10, 12, 16], "Dic3": [10, 16, 14, 6]}
result = test_even_values(d)
print(result)

# concation of two tuples
def concatenate_tuples(tuples):
Base case: if there is only one tuple, return it as a nested tuple
if len(tuples) == 1:
return (tuples[0],)

#Recursive case: concatenate the first tuple with the nested tuple of the rest of the tuples
return (tuples[0],) + concatenate_tuples(tuples[1:])

tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
result = concatenate_tuples(tuples)
print(result)


seek () and read () function
with open("myfile.txt", "r") as f:
f.seek(10)  # seek() function is start counting from the given number
print(f.tell())  # tell() function gives the current location of the file
data = f.read(5)  # read() function read the data from the given point
print(data)

Lambda Function
def mul(x):
return x * 2
def mul(x): return x * 2


print(mul(5))


MAP ,FILTER ,REDUCE
def cube(x):
   return x*x*x

l = [1, 2, 3, 4, 5]
newl = []
for item in l:
newl.append(cube(item))

newl = list(map(cube, l))
print(newl)
print(cube(2))


def filter_function(a):
   return a > 4


newnewl = list(filter(filter_function, l))
print(newnewl)
def foo(x):
x[0] = ['def']
x[1] = ['abc']
return id(x)


q = ['abc', 'def']
print(id(q) == foo(q))
liat = ['hello', 'pthhon ', 'yes ', 'safe', ]
print(min(liat))


class Sample:
    x, y = 10, 20


S = Sample()
print("Vlaue of X is ", S.x)
print("Vlaue of  is ", S.y)


class Example:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


e = Example(5, 5)
print("Sum of a , b is = ", e.add())


class student:
    def method(self):
        print("Iam method ")
        print("I was called using ", id(self))


s1 = student()
s2 = student()
print("id of s1 ", id(s1))
print("id of s2 ", id(s2))
s1.method()
s2.method()


class Student:
    mark1, mark2, mark3 = 45, 91, 71

    def process(self):
        sum = Student.mark1+Student.mark2 + Student.mark3
        avg = sum/3
        print("Total mark", sum)
        print("Average is ", avg)
        return


s = Student()
s.process()
       


class calculator:
    def addnum(x, y):
        return x+y


calculator.addnum  = staticmethod(calculator.addnum)
print("Sum is ", calculator.addnum(10, 20))
 


class Employ:
    raise1 = 1.75

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
       
     


class info:
    name = "Shubham"
    age = 19

    def about(self):
        print(f"{self.name} is {self.age} year old ")


x = info()

x.about()

        


class person:
    def __init__(self, n, m):
        self.name = n
        self.occ = m

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Shubham ", "Student")
a.info()
b = person("Shubham", "learner")

        


def the_outer_function():
    var = 10

    def the_inner_function():
        global var
        var = 14
        print("The value inside the inner function: ", var)
    the_inner_function()
    print("The value inside the outer function: ", var)


the_outer_function()

# print('This is a bell sound: \a')
# print('This is a page break:\f')
#

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [6, 7, 8, 9, 0, 1]
num_list1.extend(num_list2)
print(num_list1)

num_list2.sort()
print(num_list2)


queue = [1, 2, 3, 4, 5, 6, 7, 88]
print("Original queue is : ", queue)
queue.insert(5, 231)
print("queue after insertion :", queue)
queue.append(90)
print("After insertion queue is : ", queue)
queue.pop()
print()
print("After poping the queue : ", queue)

list = [1, 2, 3, 4, 5, 5, 3, 12, 4, 5, 2, 4, 5, 2, 4, 4]
for index, i in enumerate(list):
    print(i, "is at index ", index)


for i in range(len(list)):
    print("index is : ", i)


list = [1, 2, 3, 4, 5, 6, 7]
it = iter(list)
for i in range(len(list)):
    print("Element at index: ", i, "is:", next(it))
# for ele in it:
    # print(ele, end="  ")
#

tup = (1, 2, 3, 4, 5, 6, 7)
# len(tup)
print(len(tup))
tup2 = (2, 23, 23, 2, 3)
print(tup + tup2)
print(tup.index(4))


s = set([1, 2, 3, 4, 5])
t = set([6, 7, 89])
s.update(t)
print(s)
s.add("erer")
print(s)

s = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13])
x = ([1, 2, 3, 4, 5,])
y = ([2, 4, 6, 8, 12])
print(y <= s)
print(s >= x)
print(x | s)
"""
num = int(input("Please give a number: "))
print("Before reverse your number is : %d" % num)
rev = int(str(num)[::-1])
print("Reverse of the number : ", rev)
