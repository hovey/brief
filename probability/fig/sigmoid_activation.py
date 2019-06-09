#!/usr/bin/env python3
# sigmoid_activation.py
import numpy as np
import matplotlib as mpl
import os
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

lw = 1 # line width for leader lines

x = np.linspace(-5, 5, 100)
y = 1 / (1 + np.exp(-x))

dx = dy = 0.15

xmax = 10  # inches, width of figure
ymax =  3  # inches, height of figure

fig = plt.figure(figsize=(xmax, ymax))  # (width, height) inches 

ax = fig.add_subplot(1, 1, 1)

ax.axhline(linewidth = lw+1, color='gray', alpha=0.5)  # emphasize x-axis
ax.axvline(linewidth = lw+1, color='gray', alpha=0.5)  # emphasize y-axis
ax.plot(x, y, color='blue', linewidth = lw+1,
	label=r'$\sigma(x)$')

ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$\sigma(x)$')
ax.set_xlim(-xmax/2 - dx, xmax/2 + dx)
ax.set_ylim(-1.0 - dy, 2.0 + dy)
ax.axis('equal')
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
ax.legend(loc='upper left')

plt.show()

print_pdf = 1
if print_pdf:
  figure_name = os.path.basename(__file__).split('.')[0] + '.pdf'
  print('Saving figure to ' + figure_name)
  fig.savefig(figure_name, bbox_inches='tight')

