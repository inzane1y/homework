# emf.py

import numpy as np
from scipy import linalg

class Emf:
    '''Electromagtetic field class.'''
    __slots__ = ('_e', '_h')
    def __init__(self, e=np.zeros(3), h=np.zeros(3)):
        '''Constructor.'''
        self._e = e
        self._h = h

    def e(self, x=np.nan, t=np.nan):
        '''Get the E field in a given point.'''
        return np.array([e(x, t) if callable(e) else e for e in self._e])

    def h(self, x=np.nan, t=np.nan):
        '''Get the H field in a given point.'''
        return np.array([h(x, t) if callable(h) else h for h in self._h])

    def i(self, x, t):
        '''Get the intensity in a given point.'''
        return (linalg.norm(e(x, t)) ** 2 + linalg.norm(h(x, t)) ** 2) / (4 * np.pi)
