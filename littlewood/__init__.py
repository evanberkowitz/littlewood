name="littlewood"

import littlewood.coefficients
import littlewood.io
import littlewood.plot

from .polynomials import polynomials
from numpy.polynomial.polynomial import polyroots as roots

def ensure_roots(degree, coefficients, name="", file=None):
    try:
        return littlewood.io.read(file, name, degree)
    except:
        ...

    import numpy as np
    roots = np.array([ littlewood.roots(p) for p in littlewood.polynomials(degree, coefficients)])
    try:
        littlewood.io.write(file, name, degree, roots)
    except:
        ...
    return roots

