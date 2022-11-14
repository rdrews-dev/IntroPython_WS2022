import numpy as np
import matplotlib.pyplot as plt

def filter_data(d):
    result = []
    values = []
    for i in range(len(d)):
        v = d[i]
        if v > -9000.0:
            values.append(v)
            if len(values) == 24:
                result.append(sum(values) / 24.0)
                values = []
    return result

# Santa Gracia, 2017
data = np.loadtxt("data3.csv", delimiter=",", usecols=(1,2))

# Air temperature
result1 = filter_data(data[:, 0])

# Air relative humidity
result2 = filter_data(data[:, 1])

fig, ax = plt.subplots(2, 1)
ax[0].plot(result1)
ax[1].plot(result2)
plt.show()
