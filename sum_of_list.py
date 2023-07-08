n = int(input("Enter the size: "))
li = []
sum = 0
print("Enter the elemnt : ")
for i in range(n):
    num = int(input())
    li.append(num)
print("Element  is : ")
for i in range(n):
    print(li[i])
for i in range(len(li)):
    sum = sum + li[i]
print("Sum is : ")
print(sum)
