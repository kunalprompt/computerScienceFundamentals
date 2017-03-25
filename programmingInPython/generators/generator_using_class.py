"""
Generator using class

The three most important pointers here are:
1. __init__ to initiate the generator
2. __next__ to invoke for the next element of the generator
3. Stop generator using StopIteration Exception
"""


class Counter(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # def __iter__(self):
        # 1. In Object based Generator - iterator should return itself in __iter__
        # 2. for and in statements usage is supported by the Object based Generators
        # return self

    def __next__(self):
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
