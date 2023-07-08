# Getter and Setter Method
class one:

    def set(self, var):
        self.var = var

    def get(self):
        return self.var


class two:

    def __init__(self, var):
        self.o = one()
        self.o.set(var)

    def show(self):
        print("Number : ", self.o.get())


t = two(1000)
t.show()
