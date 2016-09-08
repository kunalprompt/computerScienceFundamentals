from functools import wraps


def decorator_function(func):
    @wraps(func)
    def plus_five_wrapper(value):
        f = func(value+5)
        return f
    return plus_five_wrapper

@decorator_function
def summition(value):
    return value

s = summition(10)
print(s, summition.__name__)
