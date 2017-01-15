import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# x_range, y_range = np.linspace(-10, 10, 100), np.linspace(-10, 10, 100)
# x, y = np.meshgrid(x_range, y_range)
# 
# z = 0.5*(1 - x - 2*y)
# ax.plot_surface(x, y, z)
# 
# x2, y2 = np.meshgrid(x_range, y_range)
# z2  = 0
# ax.plot_surface(x2, y2, z2)
# 
# y3, z3 = np.meshgrid(x_range, y_range)
# x3 = 0
# ax.plot_surface(x3, y3, z3)
# 
# x4, z4 = np.meshgrid(x_range, y_range)
# y4 = 0
# ax.plot_surface(x4, y4, z4)

# Solve Pairs of 3 equations.
# x + 2y + 2z = 4, x = 0, y = 0 => z = 2 (0, 0, 2)
# x + 2y + 2z = 4, y = 0, z = 0 => x = 4 (4, 0, 0)
# x + 2y + 2z = 4, x = 0, z = 0 => y = 2 (0, 2, 0)
# x =0, y = 0, z = 0 => (0, 0, 0)

pool =['#12efff','#eee111',
        '#eee00f','#e00fff','#123456','#abc222','#000000','#123fff','#1eff1f','#2edf4f','#2eaf9f','#22222f',
                '#eeeff1','#eee112','#00ef00','#aa0000','#0000aa','#000999','#32efff','#23ef68','#2e3f56','#7eef1f','#eeef11']

ax.set_xlim3d(0,4)
ax.set_ylim3d(0,3)
ax.set_zlim3d(0,3)

np.random.seed(1023)

corners = [(0, 0, 2), (4, 0, 0), (0, 2, 0), (0, 0, 0)]
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        p = corners[i]
        q = corners[j]
        #ax.plot(*list(zip(p, q)))

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        for k in range(j+1, len(corners)):
            p = corners[i]
            q = corners[j]
            r = corners[k]
            vtx = np.array([p, q, r])
            triangle = Poly3DCollection([vtx])
            color = np.random.randint(len(pool))
            triangle.set_color(pool[color])
            ax.add_collection3d(triangle)


plt.show()
