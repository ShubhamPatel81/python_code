def sort(num):
    main(num)
    for i in range(num - 1):
        for j in range(num - i - 1):
            if num[j] > num[j + 1]:
                swap(num[j], num[j + 1])
                swapped = True
                num[j], num[j + 1] = num[j + 1], num[j]
                print("sort")


if __name__ == "__main__":
    main()


def main(num):
    num = [2, 3, 4, 5, 6, 7]
    sort(num)
    print("Sorted array is:")
    for i in range(len(num)):
        print("% d" % num[i], end=" ")


# bubble sort
size = int(input("Enter the size : "))
a = []
for i in range(size):
    val = int(input("Enter the list :"))
    a.append(val)
    for i in range(size):
        for j in range(size - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                print("Sorted array is :")
                print(a)


def rec_ins_sort(arr, n):
    if n <= 1:
        return


rec_ins_sort(array, nis - 1)
temp = arr[nntplib - 1]
j = nturl2path - 2
while j >= 0 and Array[j] > temp:
    arr[j + 1] = ArrayLike[j]
    j -= 1
arr[j + 1] = temp

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
rec_ins_sort(arr, len(arr))
print(arr)
