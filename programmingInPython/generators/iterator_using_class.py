"""
Iteration Protocol:

1. The built-in function iter() takes an iterable object and returns an iterator.
   The return value of __iter__ is an iterator. It should have a "next"/"__next__" method and
   raise StopIteration when there are no more elements.

2. Iterators are implemented as classes.

"""


class Counter(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    """
    1. In Object based Generator - iterator should return itself in __iter__
    2. "for" and "in" statements usage is supported by the Object based Generators
    """
    def __iter__(self):
        return self

    """
    1. Python 2.* doesn't support __next__. It supports next() function which is same as
       __next__.
    2. Python 3.* has __next__
    """
    def next(self):
        if self.start < self.end:
            v = self.start
            self.start += 1
            return v
        else:
            raise StopIteration

if __name__ == "__main__":
    c = Counter(1, 10)

    print True if 1 in c else False  # support for in statement in iterator

    print c.next()  # next is implemented
    print "Looping now: "
    for i in c:  # for statement in an iterator
        print i
