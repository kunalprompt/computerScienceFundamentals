# Generator using Python Function


def generate5multiples(max_limit):
    start = 1
    while start < max_limit:
        yield start*5
        start += 1

d = generate5multiples(10)  # d is a generator
for i in d:
    print i


"""
It is the best use case because we are not storing any list in the memory.
However the following is not the best way, because we'll be storing list in memory of generator.

def generate5multiples(max_limit):
    for i in range(max_limit):
        yield i*5

"""