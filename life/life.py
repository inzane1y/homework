import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def iterate_frame(i):
    image.set_array(iterate(z))

def iterate(z):
    '''
    Returns the next step of the game.
    '''
    # Get the neighbour amount for each cell
    n = (
        np.roll(z, 1, 0) + np.roll(z, -1, 0) + 
        np.roll(z, 1, 1) + np.roll(z, -1, 1) +
        np.roll(z, (1, 1), (0, 1)) + np.roll(z, (1, -1), (0, 1)) +
        np.roll(z, (-1, 1), (0, 1)) + np.roll(z, (-1, -1), (0, 1))
    )

    birth = (n == 3) & (z == 0)
    survive = ((n == 2) | (n == 3)) & (z == 1)

    z[:] = 0
    z[birth | survive] = 1

    return z

# Side size
n = 100
# Initial matrix
z = np.random.randint(0, 2, (n, n))

# Add figure and axes
fig, ax = plt.subplots()
# Create main changing object
image = ax.matshow(z)

# Setup animation
animation = FuncAnimation(fig, iterate_frame, interval=5)

# Show what we got
plt.show()
