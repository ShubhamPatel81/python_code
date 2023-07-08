# One class access more then two parent class
class base1(object):

    def __init__(self):
        super(base1, self).__init__()
        print("This is base 1 class ")


class base2(object):

    def __init__(self):
        super(base2, self).__init__()
        print("This is base 2 class ")


class derived(base1, base2):

    def __init__(self):
        super(derived, self).__init__()
        print("Derived class ")


d = derived()
