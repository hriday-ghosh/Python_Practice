
# Multiple_Classes:

# Class No. 1
class xyz:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Method: 01 of xyz class
    def test(self):
        print("This is the method of XYZ Class")

# Class No. 2


class xyz1:
    def __init__(self, p, q, v):
        self.p = p
        self.q = q
        self.v = v
    # Method: 02 of xyz1 class

    def test1(self):
        print("This is a method of test1")

# Here we want output regarding multiple class

# Asking for child class which is asking both parents classes,  xyz1 and xyz


class child(xyz1, xyz):
    # *args means multiple arguments or multipl varibale we can pass
    def __init__(self, *args):
        xyz.__init__(self, *args)
        xyz1.__init__(self, *args)


n = child(5, 7, 8)

n.p

"""
Output 01-> This is the method of XYZ Class
for -> n = child(5, 7, 8)

Output 02:
n.test1()
for 
This is a method of test1

Output 03:

"""
