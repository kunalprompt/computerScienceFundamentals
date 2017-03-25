"""
Generator using class

Remember - Generator follows the iterator protocol. Every generator is an iterator.
Understand from iterator_using_class.py

The three most important pointers here are:
1. __init__ to initiate the generator
2. next/__next__ to invoke for the next element of the generator in Py2, Py3
3. Stop generator using StopIteration Exception
4. Must follow the Iterator Protocol
"""


class Counter(object):
    def __init__(self, end):
        self.start = 0
        self.end = end

    def __iter__(self):
        return self

    def next(self):
        if self.start < self.end:
            v = self.start
            self.start += 1
            return v
        else:
            raise StopIteration

c = Counter(10)
for i in c:
    print i
