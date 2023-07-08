# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.


class base1(object):

    def __init__(self):
        print("This is base class 1 ")


class base2(object):

    def __init__(self):
        print("This is base class 2 ")


class derived(base1, base2):
    pass


d = derived()
