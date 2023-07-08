class student:

    def method(self):
        print("I am method :")
        print("I was called by : ", id(self))


s1 = student()
s2 = student()
print("id of s1 is : ", id(s1))
print("Id of s2 is : ", id(s2))
s1.method()
s2.method()
