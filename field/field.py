#!python

import sys
import numpy as np
from scipy import linalg, integrate
import matplotlib.pyplot as plt

def f(t, p):
    '''Function f in p = f(t, p).'''
    m, c, h = 1, 1, 1 # Constants
    E, H = np.array([1, 0, 0]), np.array([0, 1, 0]) # Fields

    return np.r_[
        (m * c ** 2 / h) ** 2 * (E + np.cross(p[:3], H) / np.sqrt(1 + linalg.norm(p[:3]) ** 2)),
        p[:3] / np.sqrt(1 + linalg.norm(p[:3]) ** 2)
    ]

def main(t0, t1):
    '''Programm starts here.'''
    px0 = [0, 0, 0, 0, 0, 0] # Initial conditions
    timespan = np.r_[t0:t1:100j] # Set points for p evaluation

    x = integrate.solve_ivp(f, (t0, t1), px0, t_eval=timespan).y[3:] # Get x vector

    plt.plot(x[0], x[2]) # Plot z(x)
    plt.show()

if len(sys.argv) == 3:
    main(int(sys.argv[1]), int(sys.argv[2]))
else:
    print('Not enough arguments.')
