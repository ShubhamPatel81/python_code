# Example of inheritance in python - One class inherit all properties of another class
# 1 - Single inheritance
# 2 - Multiple inheritance
# 3 - Multilevel inheritance
# 4 - Hierarchical inheritance
# 5 - Hybrid Inheritance


class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name is : ", self.name)
        print("Age is : ", self.age)


class teacher(person):

    def __init__(self, name, age, rs, exp):
        person.__init__(self, name, age)
        self.rs = rs
        self.exp = exp

    def displaydata(self):
        person.display(self)
        print("resurch in : ", self.rs)
        print("Experiment in : ", self.exp)


class student(person):

    def __init__(self, name, age, branch, hobbis):
        person.__init__(self, name, age)
        self.branch = branch
        self.hobbis = hobbis

    def displaydata(self):
        person.display(self)
        print("Hobbis is : ", self.hobbis)
        print("Branch is : ", self.branch)


print("Teacher is ####################################")
t = teacher("ram", 45, "Chemistery", "litmus papaer")
t.displaydata()
print("Student sisisisisisiisisiisisisisiisisisisisisiisiiiiisiisiiisiis")
s = student("Shubham", 20, "CSE ", "Nothing ")
s.displaydata()
