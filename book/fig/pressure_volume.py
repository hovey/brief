"""
Demo of axis spines
from matplotlib.org/examples/ticks_and_spines/spines_demo.html

Reference:
http://matplotlib.org/examples/pylab_examples/subplots_demo.html
http://matplotlib.org/users/usetex.html
http://matplotlib.org/users/customizing.html
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('grid', linestyle='dotted', color='gray')

offset = 0.1
size = 5

V = np.array([1,1]) 
P = np.array([1,4]) 

plt.plot(V[0], P[0], 'bo')
plt.plot(V[1], P[1], 'ro')
plt.axis([0, size, 0, size])
plt.grid(True)
plt.axes().set_aspect('equal')
plt.axes().set_xticks(np.arange(0, size+1, 1))
plt.axes().set_xticklabels(['0',r'$V_0=V_1$'])
plt.axes().set_yticks(np.arange(0, size+1, 1))
plt.axes().set_yticklabels(['0',r'$P_0$','','',r'$P_1$'])
plt.xlabel(r'Volume ($V$)')
plt.ylabel(r'Pressure ($P$)')
#plt.title(r'reference configuration ($t=t_0$)')

plt.axes().annotate('initial state', xy=(V[0],P[0]), xycoords='data', 
  xytext=(V[0] + offset, P[0] - 2*offset), textcoords='data')

plt.axes().annotate('final state', xy=(V[1],P[1]), xycoords='data',
  xytext=(V[1] + offset, P[1] + offset), textcoords='data')

plt.axes().annotate('', xy=(V[1], P[1]), xycoords='data',
  xytext=(V[0], P[0]), textcoords='data',
  arrowprops=dict(facecolor='black', shrink=0.02),
  horizontalalignment='left',
  verticalalignment='top')

plt.savefig('PV_isochoric.pdf', orientation='landscape', format='pdf')

