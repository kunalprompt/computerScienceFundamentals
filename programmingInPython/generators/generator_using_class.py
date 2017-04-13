"""
Generator using class

The three most important pointers here are:
1. __init__ to initiate the generator
2. __next__ to invoke for the next element of the generator, in Py2 it is just next()
3. Stop generator using StopIteration Exception

PEP: https://www.python.org/dev/peps/pep-0234/
"""


class Counter(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # 1. In Object based Generator - iterator should return itself in __iter__
        # till that time it is not a generator/iterator
        # 2. for and in statements usage is supported by the Object based Generators
        # 3. We can also do some default initializations here.
        # 4. iter([iterable]) call should return the iterator,
        # if __iter__ is not implemented it won't return an iterator
        return self

    def next(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            raise StopIteration

c = Counter(1, 10)
# for i in c:
#     print i
print c.next()
# print 5 in c
