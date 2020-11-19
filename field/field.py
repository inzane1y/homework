#!python
# field.py

import sys
import numpy as np
from scipy import linalg, integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(t, p):
    '''Function f in p = f(t, p).'''
    m, c, h = 1, 1, 1 # Constants
    E, H = np.array([0, 1, 0]), np.array([0, 0, 1]) # Fields

    return np.r_[
        (m * c ** 2 / h) ** 2 * (E + np.cross(p[:3], H) / np.sqrt(1 + linalg.norm(p[:3]) ** 2)),
        p[:3] / np.sqrt(1 + linalg.norm(p[:3]) ** 2)
    ]

def main(t0, t1):
    '''Programm starts here.'''
    px0 = [0.001, 0.5, 0, 0, 0, 0] # Initial conditions in the form [px, py, pz, x, y, z]
    timespan = np.r_[t0:t1:100j] # Set points for p evaluation

    x = integrate.solve_ivp(f, (t0, t1), px0, t_eval=timespan).y[3:] # Get x vector

    # Get exact solution ------------------------------------------
    p0 = px0[:3]
    EH = 1
    alpha = np.sqrt(1 + np.dot(p0,p0)) - p0[0] # Integral of motion
    eps = 1 + p0[2]*p0[2] # Constant parameter

    p2_data = np.linspace(p0[1], p0[1]+10, 64) # Momentum p2
    time_data = p2_data * (eps**2-alpha**2)/(2*EH*alpha**2) + p2_data**3 / (6*EH*alpha**2)

    # Here are the solutions
    x1_exact_data = p2_data * (eps**2-alpha**2)/(2*EH*alpha**2) + p2_data**3 / (6*EH*alpha**2)
    x2_exact_data = p2_data**2 / (2*EH*alpha)
    x3_exact_data = p2_data * p0[2]/(EH*alpha)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x[0], x[1], x[2])
    ax.plot(x1_exact_data, x2_exact_data, x3_exact_data)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

if len(sys.argv) == 3:
    main(int(sys.argv[1]), int(sys.argv[2]))
else:
    print('Not enough or too much arguments.')
