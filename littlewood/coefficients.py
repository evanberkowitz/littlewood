
import numpy as np

def littlewood():
    return np.array([+1, -1])

def roots_of_unity(n):
    return np.exp(2j*np.pi/n * np.arange(n))

def integers(n):
    return np.arange(-n, n+1)

def gaussian_integers(n):
    return np.array([ a+1j*b for a in integers(n) for b in integers(n) ])
