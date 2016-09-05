from math import factorial


def combination(n, r):
    return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))


def pascals_triangle(k):
    for count in range(k):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        print " ".join("{}".format(n) for n in row)

pascals_triangle(20)
