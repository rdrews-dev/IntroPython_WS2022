import numpy as np
import matplotlib.pyplot as plt

def filter_data(d):
    result = []
    for i in range(len(d)):
        v = d[i]
        if v > -9000.0:
            result.append(v)
    return result

def derivative(d):
    result = []
    for i in range(len(d) - 1):
        result.append((d[i + 1] - d[i]) / 1.0)
    return result

# Santa Gracia, 2018
data = np.loadtxt("data4.csv", delimiter=",", usecols=(1,2))

# wind speed average
result1 = filter_data(data[:, 0])
result1_a = derivative(result1)
result1_b = derivative(result1_a)

# wind speed max
result2 = filter_data(data[:, 1])
result2_a = derivative(result2)
result2_b = derivative(result2_a)

fig, ax = plt.subplots(6, 1)
ax[0].plot(result1)
ax[1].plot(result1_a)
ax[2].plot(result1_b)
ax[3].plot(result2)
ax[4].plot(result2_a)
ax[5].plot(result2_b)
plt.show()
