from functools import wraps


def make_adder(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        f = func(*args, **kwargs)
        return f
    return wrapper_function

d = make_adder(lambda: "Hello India")
print(d())
print(d.__name__)  # wraps updates the wrapper proper
