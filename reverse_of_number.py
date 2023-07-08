# Finding the reverse of the input number
# input the number
num = int(input("Enter the number "))
print("number before reversing is : ", num)
reverse = 0
while num != 0:
    # reversing the number
    reverse = reverse * 10 + num % 10
    num = num // 10
print("After reversing the number : ", reverse)
