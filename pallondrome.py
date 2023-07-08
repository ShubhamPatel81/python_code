# Pallondrome number is a number whic is same from writting from starting  and writting from ending . Example - 121 , if we write 121 opposite we get same number .
n = int(input("enter the number "))
reverse = 0
temp = n
while temp != 0:
    reverse = temp % 10 + reverse * 10
    temp = temp // 10
if reverse == n:
    print("Number is pallondrome ")
else:
    print("Number is not a pallondrome ")
