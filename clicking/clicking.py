#
# An example demonstrating interactive clicking
#
import matplotlib.pyplot as plt
import numpy as np


my_x = np.linspace(-5, 5, 100)
my_map = np.random.rand(10, 10)


class PointMover:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 2, figsize=(8, 3))
        self.ax[0].set_title('click somewhere on the map')
        #
        # Some map. Replace it with your own.
        #
        cax = self.ax[0].imshow(my_map, origin='lower',
                                cmap='inferno')
        plt.colorbar(cax, ax=self.ax[0])
        #
        # Create the clicking point
        #
        self.point, = self.ax[0].plot([0], [0], 'c*')
        plt.show()
        #
        # Link the class to clicking event
        #
        self.cid = \
            self.point.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        #
        # Grab clicking event information
        #
        print('click', event)
        if event.inaxes != self.point.axes:
            return
        j, i = int(round(event.xdata)), int(round(event.ydata))
        #
        # Update pointer position in the first axis
        #
        self.point.set_data(j, i)
        self.point.figure.canvas.draw()
        #
        # Clear the other axes. Avoid nan / inf problem here if you want.
        #
        self.ax[1].clear()
        if not np.isfinite(my_map[i, j]):
            return
        #
        # Update the other axes. Replace it with what you want.
        #
        self.ax[1].set_title('y=sin(' + str(i) + 'x+' + str(j) + ')')
        self.ax[1].plot(my_x, np.sin(i * my_x + j))
        plt.draw()


pointmover = PointMover()
