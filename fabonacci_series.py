# Finding the fabonacci series of the given number
# Using iterative method
# n = int(input("please give a number for fibonacci series : "))
"""
first, second = 0, 1
print("fibonacci series are : ")
for i in range(0, n):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result)
"""

# using recursive method


def fibo(n):
    if n <= 0:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


fi = int(input("Enter the number "))
for i in range(fi):
    print(fibo(i))

# Anothee way ton wite this code
'''
# fibonacci series
n = int(input("Enter the number for finding fibonacci series :"))
x = 0
y = 1
z = 0
while (z <= n):
  print(z)
  x = y
  y = z
  z = x + y
# code is complete = in fibonacci series the sum of upper two number is equal to the next number
# Example = 0,1,1,2,3,4,5,6,7,8.....
'''
