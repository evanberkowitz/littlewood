import h5py as h5
import numpy as np

def dataset(name, degree):
    return "{0}/{1}".format(name,degree)

def read(file, name, degree):
    with h5.File(file, 'r') as f:
        return np.array(f[dataset(name, degree)])

def write(file, name, degree, roots):
    with h5.File(file, 'a') as f:
        f[dataset(name, degree)] = roots
