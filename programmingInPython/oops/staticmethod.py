"""
A staticmethod is just a like a function defined inside a class.
It doesn't know anything about the class or instance it was called on
and only gets the arguments that were passed without any implicit first argument.

A method which does not have any information about class.

Properties of a staticmethod:
1. definition remains same across class methods - ie a
staticmethod is created only once.
2. Can be called with the class instance or the class itself.
3. No self argument.
4. can be inherited.
"""


class Addition(object):

    def __init__(self, number):
        self.number = number

    @staticmethod
    def add_one(num):
        return num + 1

    def get_number(self):
        print(Addition.add_one)
        return self.number

    def set_number(self, number):
        print(Addition.add_one)
        self.number = number
        return self.number

a = Addition(4)

# can be called with class as well as instance
print a.add_one(2)
print Addition.add_one(5)

# function definition remains same across all instance methods - staticmethod is created only once.
print a.get_number()
print a.set_number(10)
