import numpy as np
import pylab as plt

Data = np.loadtxt('../../Data/monthly_in_situ_co2_mlo_ready4loading.txt')
print(f'The dimensions of the time series are {Data.shape}')
print(f'We have {len(Data[:,0])} data values.')
print(f'The mean value of Co2 is at the moment {np.mean(Data[:,1])} ppm which seems low.')
print(f'The standard deviation Co2 is at the moment {np.std(Data[:,1])} ppm which seems high.')

fig,ax = plt.subplots()
ax.plot(Data[:,0],Data[:,1])
ax.set(xlabel='Time in years', ylabel='Co2 in ppm', title='Keeling Curve')

fig,ax = plt.subplots()
ax.plot(Data[0:10,0],Data[0:10,1],'r-x')
ax.set(xlabel='Time in years', ylabel='Co2 in ppm', title='Keeling Curve first ten samples')

fig,ax = plt.subplots()
ax.plot(Data[-11:-1,0],Data[-11:-1,1],'r-x')
ax.set(xlabel='Time in years', ylabel='Co2 in ppm', title='Keeling Curve last ten samples')
plt.show()
