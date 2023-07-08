# Example of armstrong number like 153 = 1^3 + 5^3 + 3^3

num = int(input("Enter the number "))
sum = 0
temp = num
count = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + digit**count
    temp = temp // 10
if num == sum:
    print("Its an armstrong number ")
else:
    print("It is not armstrong number ")
