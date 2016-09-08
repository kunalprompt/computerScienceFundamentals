class LoggerDecorator(object):

    def __init__(self, f):
        self.fxn = f

    def __call__(self, *args, **kwargs):
        print(">>>{} is called.".format(self.fxn.__name__))
        return self.fxn(*args, **kwargs)


@LoggerDecorator
def summition(*args, **kwargs):
    return sum(args)

@LoggerDecorator
def sting_concatenation(a, b):
    return "{} {}".format(a, b)

print summition(1, 2, 3)
print sting_concatenation("Kunal", "Sharma")
