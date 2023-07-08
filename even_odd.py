# Check number either even or odd
class even_odd:

    def check(self, num):
        if num % 2 == 0:
            print("This number is even number ")
        else:
            print("This is odd number ")


e = even_odd()
x = int(input("Enter the number : "))
e.check(x)
