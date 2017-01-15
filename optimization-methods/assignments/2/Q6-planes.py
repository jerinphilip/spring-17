import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_range, y_range = np.linspace(-10, 10, 100), np.linspace(-10, 10, 100)
x, y = np.meshgrid(x_range, y_range)

z = 0.5*(1 - x - 2*y)
ax.plot_surface(x, y, z)

x2, y2 = np.meshgrid(x_range, y_range)
z2  = 0
ax.plot_surface(x2, y2, z2)

y3, z3 = np.meshgrid(x_range, y_range)
x3 = 0
ax.plot_surface(x3, y3, z3)

x4, z4 = np.meshgrid(x_range, y_range)
y4 = 0
ax.plot_surface(x4, y4, z4)
plt.show()
