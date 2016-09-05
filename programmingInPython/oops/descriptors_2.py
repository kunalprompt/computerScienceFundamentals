from descriptors_1 import Field


class StringField(Field):

    def __init__(self, min_length=6, max_length=16):
        self._min_length = min_length
        self._max_length = max_length
        super(StringField, self).__init__()

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Not a str instance")
        if len(value) < self._min_length or \
                len(value) > self._max_length:
                    raise ValueError("Invalid length of input {}".
                                     format(value))
        self._property = value


class EmailField(Field):

    def __init__(self, required=False):
        self._required = required
        super(EmailField, self).__init__()

    def __delete__(self, instance):
        if self._required:
            raise StandardError("A required Field can not be deleted.")
        super(EmailField, self).__delete__(instance)


class User(object):
    email = EmailField(required=True)
    fname = StringField(min_length=5, max_length=16)
    lname = StringField(max_length=10)

    def __init__(self, email, fname, lname):
        self.email = email
        self.fname = fname
        self.lname = lname


user = User(email="kunalsharma@gmail.com", fname="Kunal", lname="Sharma")
print(user.email, user.fname, user.lname)
# Avoiding any of the constraint defined above will raise corresponding error, example
# del user.email
