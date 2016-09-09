from functools import wraps


def decorator_function(arg1):

    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args):
            return func(*args)

        return inner_wrapper

    return outer_wrapper


@decorator_function("Hello World")
def fxn(*args):
    return sum(args)


f = fxn(1, 2, 3, 4)
print(f, fxn.__name__)
