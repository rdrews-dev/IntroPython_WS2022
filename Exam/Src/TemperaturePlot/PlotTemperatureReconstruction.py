import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

data = np.loadtxt('GAST.txt')
data2 = np.loadtxt('Full_ensemble_median_and 95pct_range.nh.txt');
nanval=-999;
rr=166.0/255.0
gg=188/255.0
bb=255/255.0

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(data[:,0],data[:,3],color=[rr, gg, bb])
ax1.invert_xaxis()
ax1.set_ylabel('Temperature anomaly ($^{\circ}$C)')
ax1.set_xlabel('Time before present (1000 years)')
ax1.set_ylim([-5,5])
line1=ax2.plot(data2[data2[:,5]>nanval,0],data2[data2[:,5]>nanval,5],'r.')
line2=ax2.plot(data2[data2[:,6]>nanval,0],data2[data2[:,6]>nanval,6],color=[rr, gg, bb])
ax2.set_ylim([-0.5,0.5])
ax2.legend(['Instrumental Record', 'Reconstructions'])
#ax2.plot(data2[data2[:,7]>nanval,0],data2[data2[:,7]>nanval,7])
ax2.set_xlabel('Time CE (years)')
ax2.yaxis.tick_right()
ax1.text(2000,-4.5,'Synder (Nature, 2016)')
ax2.text(0,-0.45,'PAGES 2K (incl. Rehfeld,\nNature Geoscience, 2019)')
for pos in [ 'top', 'left']:
    ax2.spines[pos].set_visible(False)
for pos in [ 'right', 'top']:
    ax1.spines[pos].set_visible(False)
plt.tight_layout()
plt.gcf().subplots_adjust(bottom=0.2)
fig.set_size_inches(10, 3)
fig.savefig('TemperatureCurves.png', dpi=300,transparent=True)
