class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name is : ", self.name)
        print("Age is : ", self.age)


class teacher(person):

    def __init__(self, name, age, exp, r_area):
        person.__init__(self, name, age)
        self.exp = exp
        self.r_area = r_area

    def displaydata(self):
        person.display(self)
        print("Experiment is : ", self.exp)
        print("Resurch area is : ", self.r_area)


class student(person):

    def __init__(self, name, age, course, marks):
        person.__init__(self, name, age)
        self.course = course
        self.marks = marks

    def displaydata(self):
        person.display(self)
        print("Course is : ,", self.course)
        print("Marks is : ", self.marks)


print("$$$$$$$$$$$$ teacher $$$$$$$$")
t = teacher("Guru ", 45, 23, "java application")
t.displaydata()

print("############## Student  ###########")
k = student("Shubham", 19, "python", 87)
k.displaydata()
