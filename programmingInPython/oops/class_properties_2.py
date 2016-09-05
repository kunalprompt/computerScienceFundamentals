# ---------------------------------------------------------------------------
# Method - 2: Defining Properties of a class using @property
# ---------------------------------------------------------------------------


class Celcius2(object):

    def __init__(self, value=None):
        self.temprature_value = value

    @property
    def temprature_value(self):
        return self._temprature

    @temprature_value.setter
    def temprature_value(self, value):
        if value < -273:
            raise ValueError
        self._temprature = value

    @temprature_value.deleter
    def temprature_value(self):
        self._temprature = None

    def convert_to_farenheit(self):
        if not self._temprature:
            raise ValueError("Temprature is not valid.")
        return self._temprature*1.8 + 32

c = Celcius2(50)
print('Celcius {} | Farenheit {}'.format(c.temprature_value,
                                         c.convert_to_farenheit()))

# update a data member by use of property
c.temprature_value = -150
print('Celcius {} | Farenheit {}'.format(c.temprature_value,
                                         c.convert_to_farenheit()))

# deleting a data member by use of property
del c.temprature_value
print('Celcius {}'.format(c.temprature_value))

# this will throw ValueError now
# c.convert_to_farenheit()

# what about the following?
# c = Celcius(-500)
