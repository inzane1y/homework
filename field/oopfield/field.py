#! python
# field.py

import numpy as np
from scipy import integrate, linalg
from emf import Emf
from particle import Particle

p = Particle(1, -1, p=[0.1, 0, 0]) # Particle initialization
f = Emf([0, 0, 0], [0, 1, 0]) # Field from a previous task
f2 = Emf([lambda x, t: np.cos(t - x[2]), 0, 0], [0, lambda x, t: np.sin(t - x[2]), 0]) # EM wave

t_i = 0
t_f = 10
p.solve(f, t_i, t_f, timespan=np.r_[t_i:t_f:1000j]) # Solve the system
# p.plot('pzt') # Print result

p.plotInField(f)

# f2.plot('ex', -5, 5, 'ztxy', 0, 0)

