import numpy as np
import matplotlib.pyplot as plt

def filter_data(d):
    result = []
    for i in range(len(d)):
        v = d[i]
        if v > -9000.0:
            result.append(v)
    return result


# Santa Gracia, 2018
data = np.loadtxt("data5.csv", delimiter=",", usecols=(1,2))

# wind speed average
result1 = filter_data(data[:, 0])

# wind speed max
result2 = filter_data(data[:, 1])

fig, ax = plt.subplots(2, 1)
ax[0].plot(result1)
ax[1].plot(result2)
plt.show()
