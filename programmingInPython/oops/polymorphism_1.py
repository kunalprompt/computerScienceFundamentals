"""
Method overloading
"""


def summition(*args, **kwargs):
    addition_slug = int(kwargs.get('slug', 0))
    return sum(args) + addition_slug

print(summition(1, 2, 3, slug=100))
print(summition(1, 2, 3, 4, 5, slug=100))
