import numpy as np
import pylab as plt

data = np.loadtxt('XYShirase_GPS_Small.txt')
coeff = np.polyfit(data[:,0],data[:,1],1)
reg = np.polyval(coeff,data[:,0])

# print(data.shape)
plt.figure(0)
plt.plot(data[:,0],data[:,1])
plt.plot(data[:,0],reg,'r-')
plt.figure(1)
plt.plot(data[:,0],data[:,4])

plt.figure(2)
plt.plot(data[:,5])


dt=data[-1,5]-data[0,5]
ds = ((data[0,0]-data[-1,0])**2+(data[0,1]-data[-1,1])**2)**0.5
ds = ((data[0,0]-data[-1,0])**2+(reg[-1]-reg[0])**2)**0.5
print(ds)
print(f'Speed: {ds/dt*365} m per year')