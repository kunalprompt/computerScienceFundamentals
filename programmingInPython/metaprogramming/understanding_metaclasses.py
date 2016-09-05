"""
A class is an instance of a class, as class is a first class object.
If C is a class, it should have __class__. Therefore, a meta class
instance must have __class__ attribute.

Sources:
https://www.python.org/download/releases/2.2/descrintro/#metaclasses
https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/

"""


class MethodsMetaClass(type):

    def __new__(cls, name, bases, body):
        if "get" not in body:
            raise StandardError("Can not create a class with out get method.")
        return super(MethodsMetaClass, cls).__new__(cls, name, bases, body)


class ABC(object):  # I'm inherting from object which the base type class
    __metaclass__ = MethodsMetaClass  # I am an instance of MethodsMeta

    def print_metaclass_type(self):
        return MethodsMetaClass.__class__

    def print_instance_type(self):
        return type(self)

    def get(self):
        pass

a = ABC()
print("A dict - ", a.__dict__)
print("ABC's metaclass - ", a.print_metaclass_type())
print("ABC's instance class - ", a.print_instance_type())
