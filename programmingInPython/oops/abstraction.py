"""
An abstract class is a a class:
1. That creates a template for all its subclasses.
2. Cannot be instantiated.
3. Need to be extended/implemented only in child classes.
"""
from abc import ABCMeta, abstractmethod, abstractproperty


class Animal:
    __metaclass__ = ABCMeta
    # to make is python 3.* compatible pass *metaclass=ABCMeta* as argument to class
    # because Python 3.* ignores __metaclass__ attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

# to below line will raise TypeError
# a = Animal()


# implementing abstract class
class Dog(Animal):

    # abstraction may also contain some method which already may have implementation
    def __init__(self, name, age):
        super(Dog, self).__init__(name, age)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog('Boxy', 1)
print('Hi I am {}. I am {} years old.'.format(d.get_name(), d.get_age()))
