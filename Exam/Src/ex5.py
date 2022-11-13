import numpy as np
import pylab as plt

data = np.loadtxt('XYIRH1.txt')
ind = np.isnan(data[:,0])
data=np.delete(data,ind,axis=0)
order= np.arange(0,len(data))
print(order.shape)
plt.scatter(data[:,0],data[:,1],s=5,c=order)
plt.show()
