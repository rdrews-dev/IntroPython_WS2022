import numpy as np
import matplotlib.pyplot as plt

lenX = 100
lenY = 100

x = np.linspace(0, lenX)
y = np.linspace(0, lenY)
xx, yy = np.meshgrid(x, y)

A = 1.0
x0 = 50.0
y0 = 50.0
sig_x = 400.0
sig_y = 400.0

t1 = ((xx - x0)**2) / sig_x
t2 = ((yy - y0)**2) / sig_y
zz = A * np.exp(-t1 - t2)

fig, ax = plt.subplots()
ax.pcolormesh(xx, yy, zz)
plt.show()
