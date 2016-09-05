"""
What is better to use a descriptor or @property?

Sources:
https://docs.python.org/3/howto/descriptor.html
http://www.ibm.com/developerworks/library/os-pythondescriptors/
"""


class Field(object):

    def __init__(self):
        self._property = None

    def __get__(self, instance, owner):
        return self._property

    def __set__(self, instance, value):
        self._property = value

    def __delete__(self, instance):
        self._property = None


class Person(object):
    fname = Field()
    lname = Field()

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

user = Person("Kunal", "Sharma")
print(user.fname)
print(user.lname)
