# plotter.py

import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class Plotter:
    def _plot3d(self, x, axnames=['x', 'y', 'z']):
        '''Plots 3D graph.'''
        if len(axnames) != 3:
            raise ValueError('Argument axnames must contain 3 strings.')

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x[0], x[1], x[2])

        ax.set_xlabel(axnames[0])
        ax.set_ylabel(axnames[1])
        ax.set_zlabel(axnames[2])

        plt.show() # Show the plot

    def _plot2d(self, x, axnames=['x', 'y']):
        '''Plots 2D graph.'''
        if len(axnames) != 2:
            raise ValueError('Argument axnames must contain 2 strings.')

        fig, ax = plt.subplots()
        ax.plot(x[0], x[1])

        ax.set_xlabel(axnames[0])
        ax.set_ylabel(axnames[1])

        plt.show() # Show the plot

    def plot2dcmap(self, x, y, z, axnames=['x', 'y'], title='Figure'):
        '''Plots gradient colors.'''
        fig, ax = plt.subplots()
        plt.title(title)
        cs = ax.contourf(x, y, z, levels=50, cmap='spring')
        cbar = plt.colorbar(cs)
        ax.set_xlabel(axnames[0])
        ax.set_ylabel(axnames[1])
        plt.show()

    def plot(self, x, axnames=['x', 'y', 'z'], dim=3):
        '''Plots the stuff out.'''
        if dim == 3:
            self._plot3d(x, axnames=axnames)
        elif dim == 2:
            self._plot2d(x, axnames=axnames)
