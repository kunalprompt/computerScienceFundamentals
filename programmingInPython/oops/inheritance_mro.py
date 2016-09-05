class A:
    pass


class B:
    pass


class C:
    pass


class X(A, B):
    pass


class Y(B, C):
    pass


class Z(Y, X, C):
    pass


if __name__ == '__main__':
    print help(Z)
