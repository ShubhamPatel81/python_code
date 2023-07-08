# Creating Employee Name and ID
class student:
    count = 0

    def __init__(self, name):
        student.count += 1
        self.name = name
        self.count = student.count

    def __str__(self):
        return str(self.count) + " " + self.name


sl = [student("shubham"), student("Rohit "), student("golu")]
for ele in sl:
    print(ele)
