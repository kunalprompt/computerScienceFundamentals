"""
Classmethod is facility which exposes class data to the outside world.
It has complete information about the class.

Properties of a classmethod:
1. definition is associated with class.
2. Can be called with the class instance or the class itself.
3. No self argument but accepts class as its first argument.
4. can be inherited.
"""


class A(object):
    instances = 0

    def __init__(self, number):
        self.number = number
        A.instances += 1  # accessing class variable which already been created

    @classmethod
    def count_instances(cls):
        return cls.instances


a = A(10)
print A.count_instances()
print a.count_instances()

b = A(20)
print A.count_instances()


class B(A):
    pass

c = B(10)
print B.count_instances()
