#! python
# field.py

import numpy as np
from scipy import integrate, linalg
from emf import Emf
from particle import Particle

p = Particle(1, p=[-0.1, 0.01, -1])
f = Emf([1, 0, 0], [0, 1, 0])
f2 = Emf([lambda x, t: np.cos(t - x[2]), 0, 0], [0, lambda x, t: np.sin(t - x[2]), 0])
p.xplot(f2, 0, 100, timespan=np.r_[0:10:100j])
