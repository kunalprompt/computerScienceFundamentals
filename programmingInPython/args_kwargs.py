def args_method(*args):
    print('args - ', args)


def kwargs_method(**kwargs):
    print('kwargs - ', kwargs)


# python 2
def check_args_kwargs_py2(length, *args, **kwargs):
    # doesn't allows a regular argument after *args, you
    # cannot have - def check_args_kwargs(*args, length, **kwargs):
    # also length is a positional argument
    print(length)


# python 3 - another change in python 3
def check_args_kwargs_py3(*args, length, **kwargs):
    # look at the way argument length is passed in
    print(length)


if __name__ == '__main__':
    args_method(1, 2, 3)
    kwargs_method(name='Kunal')
    check_args_kwargs_py2(10, 1, 2, 3, name="Hello")
    check_args_kwargs_py3(1, 2, length=10, name="Hello")
