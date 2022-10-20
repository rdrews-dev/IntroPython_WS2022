import numpy as np
import pylab as plt

Data = np.loadtxt('../../Data/monthly_in_situ_co2_mlo_ready4loading.txt')
NumberOfSamples = len(Data[:,0])
#Filter negative values. Later use functions for this, e.g., np.where()
ListFilter=[]
for kk in np.arange(0,NumberOfSamples):
    if Data[kk,1]<0:
        print(f'There is a negative value in row {kk}.')
        ListFilter.append(kk)
print(f'Remove all negative values from time series.')
Data = np.delete(Data,ListFilter,0)
NumberOfSamples = len(Data[:,0])

#Approximate time derivative with forward differencing.
#This will have one data point less.
d_dt = np.zeros((NumberOfSamples,2))

for kk in np.arange(0,NumberOfSamples-1):
    d_dt[kk,0] = Data[kk,0]
    d_dt[kk,1] = (Data[kk+1,1]-Data[kk,1])/((Data[kk+1,0]-Data[kk,0]))
d_dt[NumberOfSamples-1,1]=d_dt[NumberOfSamples-2,1]
d_dt[NumberOfSamples-1,0]=Data[NumberOfSamples-2,0]

#Visualize
fig,ax = plt.subplots()
ax.plot(Data[:,0],Data[:,1])
ax.set(xlabel='Time in years', ylabel='Co2 in ppm', title='Keeling Curve')

fig,ax = plt.subplots()
ax.plot(d_dt[:,0],d_dt[:,1])
ax.set(xlabel='Time in years', ylabel='Co2 rate per year', title='Keeling Curve')
plt.show()
