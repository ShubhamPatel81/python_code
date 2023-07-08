# num = int(input("Enter any number between 0-30 : "))
# if (num >= 0 and num <= 0):
#     print("Its is in the range 0-10")
# elif (num >= 10 and num <= 20):
#     print("Its is in the range 10-20")
# elif (num >= 20 and num <= 30):
#     print("Number is between 20-30")
# else:
#     print("Out of range ")

# # Using for loop
# for i in range(1, 10):
#     print(i, end=' ')
# print("\n")

# for i in range(1, 30, 3):
#     print(i, end=" ")
# print("\n")

# for i in range(12):
#     print(i, end=" ")
# print("\n")

# for i in range(1, 15):
#     if (i == 10):
#         continue
#     print(i, end=" ")
# print("\n")

# for letter in "HELLO":
#     pass
# print("Pass", letter)
# print("\n")

# def print_pattern(n):
#     # row looping
#     for row in range(n):
#         # column looping
#         for column in range(n):
#             if (
#                     # right slanting line
#                     (row + column == n - 1 and row < n / 2) or
#                     # left slanting line
#                     (row == column and row < n / 2)
#             ):
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

# size = int(input("Enter any size: \t"))
# if size < 8:
#     print("Enter a size minimum of 8")
# else:
#     print_pattern((size * 2) + 1)

# # String
# str = "Hello!"
# index = 0
# for i in str:
#     print("string [", index, "] = ", i)
#     index = index + 1
# str_1 = " Hello"
# str_2 = " World"
# str_3 = str_1 + str_2
# print(str_3)

# a = " 1234"
# print(id(a))

# #   String are inmutable
# str1 = "Hello"
# print("str1 is : ", str1)
# print("ID of str1 is : ", id(str1))
# str2 = "World"
# print("str2 is : ", str2)
# print("ID of str2 is : ", id(str2))
# str1 = str1 + str2
# print("Str1 after concenation : ", str1)
# print("str1 ID is : ", str1)
# str3 = str1
# print("str3 : ", str3)
# print("id of fstr3 is : ", id(str3))
# str = ' hello'
# print(str.capitalize())

# using of inbuilt function

message = "He is my best friend "
print(message.find("my", 0, len(message)))

# print(message.index("mine", 0, len(message)))

message1 = " JamesBond007"
print(message1.isalnum())
print(message1.isalpha())

messa = "   "
print(messa.isspace())

pr = " HELLO"
print(pr.isupper())

print(len(pr))

print(pr.ljust(10, "*"))

print(pr.rjust(12, "*"))

print(message)

st = "Welcome to the python world "
print(st)
print(st[2:10])
print(st[2:20:2])
