# emf.py

import numpy as np
import plotter as plt
from scipy import linalg

class Emf:
    '''Electromagtetic field class.'''
    def __init__(self, e=np.zeros(3), h=np.zeros(3)):
        '''Constructor.'''
        self._e = e
        self._h = h

    def e(self, x=np.nan, t=np.nan):
        '''Get the E field in a given point.'''
        return np.array([e(x, t) if callable(e) else e for e in self._e])
    def e_alt(self, x, y, z, t, index):
        return self.e([x, y, z], t)[index]

    def h(self, x=np.nan, t=np.nan):
        '''Get the H field in a given point.'''
        return np.array([h(x, t) if callable(h) else h for h in self._h])
    def h_alt(self, x, y, z, t, index):
        return self.h([x, y, z], t)[index]

    def i(self, x, t):
        '''Get the intensity in a given point.'''
        return (linalg.norm(self.e(x, t)) ** 2 + linalg.norm(self.h(x, t)) ** 2) / (4 * np.pi)
    def i_alt(self, x, y, z, t):
        return self.i([x, y, z], t)

    def plot(self, func, x, y, proj, c1, c2): # 'yzxt'
        '''Plots intensity of the field.'''
        proj = np.array(list(proj)) # Convert proj to list of chars
        temp = np.array([ord(c) - 120 if c != 't' else 3 for c in proj])
        perm = np.empty_like(temp)
        perm[temp] = np.arange(len(temp))

        m1, m2 = np.mgrid[y:x:5j, x:y:5j] # Create a meshgrid
        m3, m4 = np.full_like(m1, c1), np.full_like(m1, c2)

        grid = np.stack((m1, m2, m3, m4)) 
        grid = grid[perm]

        if func == 'i':
            vecfunc = np.vectorize(self.i_alt)
            z = vecfunc(grid[0], grid[1], grid[2], grid[3])
        elif 'e' in func:
            vecfunc = np.vectorize(self.e_alt)
            z = vecfunc(grid[0], grid[1], grid[2], grid[3], ord(func[1]) - 120)
        elif 'h' in func:
            vecfunc = np.vectorize(self.h_alt)
            z = vecfunc(grid[0], grid[1], grid[2], grid[3], ord(func[1]) - 120)

        func = func.capitalize()
        func = list(func)
        if len(func) > 1:
            func = '$' + func[0] + '_' + func[1] + '$'

        plotter = plt.Plotter()
        plotter.plot2dcmap(m2, m1, z, axnames=proj[:2][::-1], title=func)
