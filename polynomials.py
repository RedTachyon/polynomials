import numpy as np
import matplotlib.pyplot as plt


class Polynomial:
    """
    Class representing polynomials.
    coefficients - iterable, repr. P(x) = coefficients[0] + coefficients[1] * x + ...
    """
    def __init__(self, coefficients, reverse=False):
        if reverse:
            self.coefficients = reversed(coefficients)
        else:
            self.coefficients = coefficients
        self.N = len(self.coefficients)

    def eval(self, x):
        return sum(self.coefficients[n] * x**n for n in range(self.N))

    def __str__(self):
        return ' + '.join(['%d x^%d' % (self.coefficients[n], n)
                          for n in range(self.N-1, 0, -1)
                          if self.coefficients[n] != 0] + [str(self.coefficients[0] if self.coefficients != 0 else '')])

    def __add__(self, other):
        pass

    def __call__(self, *args, **kwargs):
        assert len(args) == 1
        return self.eval(args[0])

if __name__ == '__main__':
    P = Polynomial((1, 3, 6, 4, 2, 0, 0, 3))
    print(P)
    print(P(5))