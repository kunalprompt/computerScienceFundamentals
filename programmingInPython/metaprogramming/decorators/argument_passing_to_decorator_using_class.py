from functools import wraps


class CustomLoggingDecorator(object):

    def __init__(self, arg):
        print("Custom Logging Decorator")
        self.arg = arg

    def __call__(self, func):
        print self.arg

        @wraps(func)  # this is how we can stay on the wrapped object
        def wrapper(*args, **kwargs):
            return func(*args)

        return wrapper


@CustomLoggingDecorator("Hello World")
def fxn(*args):
    return sum(args)

f = fxn(1, 2, 3, 4)
print(f, fxn.__name__)
