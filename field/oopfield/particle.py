# particle.py

import numpy as np
import plotter as plt
from scipy import integrate, linalg
from emf import Emf
from mpl_toolkits.mplot3d import Axes3D

class Particle:
    def __init__(self, m, e, x=[0, 0, 0], p=[0, 0, 0]):
        '''Constructor.'''
        self.e = e
        self.m = m
        self.x = x
        self.p = p
        self._solution = []

    # Methods ------------------------------------------------------------
    def plot(self, proj='xyz'):
        '''Plot the trajectory.'''
        if self._solution == []:
            raise ValueError('Solution is absent')
        proj = np.array(list(proj)) # ['x', 'y', 'z']
        plotter = plt.Plotter()
        pflag = proj[0] == 'p'

        if pflag:
            proj = np.delete(proj, 0)
            arg = self._solution[:4]
        else:
            arg = self._solution[4:]

        proj = proj[::-1]
        perm = [ord(c) - 120 if c != 't' else 3 for c in proj]

        if pflag: # Make p_i look pretty
            proj = ['$p_' + c + '$' if c != 't' else c for c in proj]

        plotter.plot(arg[perm, :], axnames=proj, dim=len(perm))

    def solve(self, f, t_i, t_f, timespan=None):
        '''Get coordinates and momentum in a given timespan.'''
        px0 = np.r_[self.p, self.x] # Set initial conditions as one array in the form [px, py, pz, x, y, z]
        solution = integrate.solve_ivp(self._equation, (t_i, t_f), px0, t_eval=timespan, args=(f, )) # Solve the equation and return x-values
        self._solution = np.vstack((solution.y[:3], solution.t, solution.y[3:], solution.t)) # For convenience output is [p, t, x, t]

    def _equation(self, t, px, f):
        '''Function f in px = f(t, px).'''
        return np.r_[
            self.m ** 2 * (f.e(px[3:], t) + np.cross(px[:3], f.h(px[3:], t)) / np.sqrt(1 + linalg.norm(px[:3]) ** 2)),
            px[:3] / np.sqrt(1 + linalg.norm(px[:3]) ** 2) 
        ]

    def plotInField(self, field, proj='xy'):
        '''Plots charge trajectory in field.'''
        plotter = plt.Plotter()
        field.plot('ex', -5, 5, 'xyzt', 0, 0)
        self.plot('xy')
