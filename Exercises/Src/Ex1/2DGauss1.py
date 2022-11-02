from math import exp
import numpy as np
import matplotlib.pyplot as plt

lenX = 100
lenY = 100

G = np.empty((lenX, lenY))
G.fill(0.0)

A = 1.0
x0 = 50.0
y0 = 50.0
sig_x = 400.0
sig_y = 400.0

for x in range(0, lenX):
    for y in range(0, lenY):
        t1 = ((x - x0)**2) / sig_x
        t2 = ((y - y0)**2) / sig_y
        G[x, y] = A * exp(-t1 - t2)

fig, ax = plt.subplots()
ax.pcolormesh(G)
plt.show()
