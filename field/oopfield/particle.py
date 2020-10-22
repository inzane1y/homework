# particle.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, linalg
from emf import Emf
from mpl_toolkits.mplot3d import Axes3D

class Particle:
    def __init__(self, m, x=[0, 0, 0], p=[0, 0, 0]):
        '''Constructor.'''
        self.m = m
        self.x = x
        self.p = p

    # Properties ---------------------------------------------
    @property
    def m(self):
        '''Particle's mass.'''
        return self._m

    @m.setter
    def m(self, m):
        if m < 0:
            raise ValueError('Mass cannot be negative.')
        self._m = m

    @property
    def x(self):
        '''Particle's coordinates.'''
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def p(self):
        '''Particle's momentum.'''
        return self._p

    @p.setter
    def p(self, p):
        self._p = p

    # Methods ------------------------------------------------------------
    def xplot(self, f: Emf, t_i, t_f, timespan=None):
        '''Plot the trajectory.'''
        x = self._traj(f, t_i, t_f, timespan=timespan) # Solve the equations

        # Plot setup
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x[0], x[1], x[2])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show() # Show the plot

    def _traj(self, f: Emf, t_i, t_f, timespan=None) -> np.ndarray:
        '''Get coordinates in a given timespan.'''
        self._e = f.e # Set the fields
        self._h = f.h # These are bound methods
        px0 = np.r_[self.p, self.x] # Set initial conditions as one array in the form [px, py, pz, x, y, z]
        return integrate.solve_ivp(self._equation, (t_i, t_f), px0, t_eval=timespan).y[3:] # Solve the equation and return x-values

    def _equation(self, t, px):
        '''Function f in px = f(t, px).'''
        return np.r_[
            self.m ** 2 * (self._e(px[3:], t) + np.cross(px[:3], self._h(px[3:], t)) / np.sqrt(1 + linalg.norm(px[:3]) ** 2)),
            px[:3] / np.sqrt(1 + linalg.norm(px[:3]) ** 2) 
        ]
