

import numpy as np
from .coefficients import littlewood as default_coefficients

class polynomials:
    def __init__(self, degree, coefficients=default_coefficients()):
        self.d = degree+1
        self.c = np.array(coefficients)
        self.n = len(coefficients)

        self.picks = np.zeros(self.d, dtype=int)
        self.picks[0] = -1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        for i in range(self.d):
            self.picks[i] += 1
            if self.picks[i] < self.n:
                break
            else:
                if i == self.d-1:
                    raise StopIteration()
                self.picks[i] = np.mod(self.picks[i], self.n)

        # We disallow polynomials whose leading coefficient is 0.
        # Those polynomials belong to the previous degree.
        if self.c[self.picks][-1] == 0:
            return next(self)
        return self.c[self.picks]
