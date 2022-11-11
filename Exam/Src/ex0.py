import numpy as np
import matplotlib.pyplot as plt

def filter_data(d):
    remove = []
    for i in range(len(d)):
        if d[i] < -9000.0:
            remove.append(False)
        else:
            remove.append(True)
    return d[remove]


data = np.loadtxt("data0_no_time.csv", delimiter=",")

# Air temperature
result1 = filter_data(data[:, 0])

# Solar radiation
result2 = filter_data(data[:, 1])

fig, ax = plt.subplots(2, 1)
ax[0].plot(result1)
ax[1].plot(result2)
plt.show()
