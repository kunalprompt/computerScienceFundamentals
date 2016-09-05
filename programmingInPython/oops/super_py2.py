class Animal(object):

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)
        # Remember: super(self.__class__, self)

    def get_name(self):
        return self.name

c = Cat('Meowwww Python 2')
print c.get_name()
