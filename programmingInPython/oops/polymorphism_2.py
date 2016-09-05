"""
Operator overloading
"""


class AX(object):

    def __init__(self, a, b):
        self.number = a*b

    def __le__(self, other):
        return self.number <= other.number


class BX(object):
    def __init__(self, a, b):
        self.number = a/b

    def __le__(self, other):
        return self.number <= other.number

a = AX(10, 3)

b = BX(20, 4)

print("a<=b ", a<=b)
print("b<=a ", b<=a)
