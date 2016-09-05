"""
Singleton Class: A class with just one instance is called singleton class.
"""


class A(object):
    instances = 0

    def __init__(self):
        A.instances += 1
        if A.instances > 1:
            raise TypeError("Can not create more than one instances.")


a = A()
b = A()  # this will raise exception
