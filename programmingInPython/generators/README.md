#### Important Questions

1. Generators Using Class

1.1 What is the difference between a iterable and iterator?

1.2 What is the differnce between __iter__() and __next__()?

1.3 What is the main role of __iter__()?

1.4 Describe the role of __next__()?

_PEP_: https://www.python.org/dev/peps/pep-0234/

2. Generators in Functions

2.1 Would the following generator store the whole list in memory
or how does it serves the purpose of generator?

```
def list_iterator(list):
    for i in range(list):
        yield i

```
