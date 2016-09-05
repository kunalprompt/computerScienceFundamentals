def make_adder(number):
    # the argument number is available in complete scope
    print(locals())

    def add(value):
        print(locals())
        return number+value
    return add

d = make_adder(10)
print(d(3))
print(d.__name__, "Name of the function")
