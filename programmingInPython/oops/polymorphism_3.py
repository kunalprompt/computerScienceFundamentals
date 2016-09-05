"""
Method Overriding
"""


class Animal(object):

    def __init__(self, name):
        self.name = name

    def sayhi(self):
        pass


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)

    def sayhi(self):
        print("Bowww Bowww. I am "+self.name)


class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)

    def sayhi(self):
        print("Meowww Meoww. I am "+self.name)

d = Dog('Romeo')
d.sayhi()

c = Cat('Lotti')
c.sayhi()
