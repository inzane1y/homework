# graphs.py

import percolation as pl
import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

def graph(n_list, n_experiments, n_attempts):
    for n in n_list:
        if not os.path.isfile(f'{n}x{n}_{n_experiments}_{n_attempts}.txt'):
            pl.percolation(n, n_experiments, n_attempts)

    fig, ax = plt.subplots() 
    for n in n_list:
        ax.plot(
            np.genfromtxt(f'{n}x{n}_{n_experiments}_{n_attempts}.txt', usecols=0),
            np.genfromtxt(f'{n}x{n}_{n_experiments}_{n_attempts}.txt', usecols=1),
            label=f'{n}'
        )

    ax.set_xlabel('p')
    ax.set_ylabel('P_cond')
    ax.set_title('P_cond(p)')
    ax.legend()

    plt.show()

if __name__ == '__main__': 
    if len(sys.argv) > 3:
        n = len(sys.argv)
        graph([int(n) for n in sys.argv[1:n-2]], int(sys.argv[n - 2]), int(sys.argv[n - 1]))
    else:
        raise ValueError(f'Expected at least 3 arguments: <m_size1> <m_size2> ... <n_experiments> <n_attempts>, got {len(sys.argv)}.')
