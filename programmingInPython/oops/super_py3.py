class Animal(object):

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        return self.name

c = Cat('Meowwww Python 3')
print(c.get_name())
