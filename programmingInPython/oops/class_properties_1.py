"""
Property is something which plays an important role is exposing an attribute
of the class to the outside world.

Example: For a engineer, its easy to understand that instance variable is
stored as "_temparature" in the class below, and some has some conditions on it.
But for the outside world, its considered as best practice to give simple
and easy to remember attributes. So here comes the properties to save us.

"""

# ---------------------------------------------------------------------------
# Method - 1: Defining Properties of a class
# ---------------------------------------------------------------------------


class Celcius(object):

    def __init__(self, value=None):
        self.temprature_value = value

    def get_temprature(self):
        return self._temprature

    def set_temprature(self, value):
        if value < -273:
            raise ValueError('Temprature can not be less than -273 in Celcius.')
        self._temprature = value

    def del_temprature(self):
        self._temprature = None

    temprature_value = property(get_temprature,
                                set_temprature,
                                del_temprature,
                                "temprature_value let's you to read, write, "
                                "and delete temprature value.")

    def convert_to_farenheit(self):
        if not self._temprature:
            raise ValueError("Temprature is not valid.")
        return self._temprature*1.8 + 32

c = Celcius(-400)
print('Celcius {} | Farenheit {}'.format(c.temprature_value,
                                         c.convert_to_farenheit()))

"""
Understand the difference now:

If your client directly access's *_temprature*, he can do something like
c._temprature = -300
But the validation of setting *_temprature* won't be invoked at all.
So if you expose _temprature to client, you will never be able to insert
new validations. And if you exposes the property later, client will have to
do a lot of refactoring in his code.
"""

# right approach to update a data member by use of property
# c.temprature_value = -200
# print('Celcius {} | Farenheit {}'.format(c.temprature_value,
#                                          c.convert_to_farenheit()))

# deleting a data member by use of property
# del c.temprature_value
# print('Celcius {}'.format(c.temprature_value))

# this will throw ValueError now
# c.convert_to_farenheit()
