"""
Can we delegate a generator to the next generator?
"""


def gen_1(n):
    yield n*n


def gen_2(n):
    for i in xrange(n):
        yield gen_1(i)


def generator_delegation_4_1():
   for i in xrange(10):
       print gen_2(i)

# generator_delegation_4_1()


def generator_delegation_4_2():
    for i in gen_2(10):
        # print next(i)
        for j in i:
            print j

generator_delegation_4_2()
