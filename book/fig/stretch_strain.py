#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)


rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

lw = 2  # line width

x1 = np.arange(0, 3, 0.01)   # plot limits to be [ 0, 3]
x2 = np.arange(0.01, 3, 0.01)   # plot limits to be [ 0.1, 3]

x_min_small = 0.8
x_max_small = 1.2
y_min_small = -0.2
y_max_small = 0.2

x1_small = np.arange(x_min_small, x_max_small, 0.01)   # plot limits to be [ 0, 3]

y_green_lagrange = 0.5*(x1**2 - 1.0)
y_engineering = x1 - 1.0
y_log = np.log(x2)
y_true = 1.0 - (1.0 / x2)
y_almansi_euler = 0.5*(1 - (1.0/x2)**2)

y_green_lagrange_small = 0.5*(x1_small**2 - 1.0)
y_engineering_small = x1_small - 1.0

fig = plt.figure(figsize=(6, 8))  # 6 inches wide, 8 inches tall
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
# major axes
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
# minor axes
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

bg_color = 'lightyellow'  # background color for inset
bg_x = [x_min_small, x_max_small, x_max_small, x_min_small, x_min_small]
bg_y = [y_min_small, y_min_small, y_max_small, y_max_small, y_min_small]

ax.fill(bg_x, bg_y, bg_color)
# ax.fill([1.0, 2.0, 2.0], [0, 0, 1], 'lightgray')
ax.plot(bg_x, bg_y, color='black', linestyle='-', linewidth=0.5)
ax.plot(x1, y_green_lagrange, color='green', linestyle='-', linewidth=lw, label='Green-Lagrange', zorder=2)
ax.plot(x1, y_engineering, color='blue', linestyle='--', linewidth=lw, label='engineering', zorder=4)
ax.plot(x2, y_log, color='red', linestyle='-', linewidth=lw+1, label='log (Hencky, natural)', zorder=1)
ax.plot(x2, y_true, color='cyan', linestyle='-.', linewidth=lw, label='true', zorder=3)
ax.plot(x2, y_almansi_euler, color='magenta', linestyle=':', linewidth=lw, label='Almansi-Euler', zorder=2)

ax.grid(b=True, which='major', linestyle='-')
ax.grid(b=True, which='minor', linestyle=':')
ax.set_xlabel('stretch $\lambda = \ell / L$')
ax.set_ylabel('strain $f(\lambda)$')
ax.set_xlim(0, 3)
ax.set_ylim(-2, 2)
# ax.legend(loc='lower right')
ax.legend(loc='upper left')

ax2 = plt.axes([0.457, 0.143, 0.45, 0.35])
ax2.axis('equal')
# major axes
ax2.xaxis.set_major_locator(MultipleLocator(1.0))
ax2.xaxis.set_ticklabels([])  # turn off xtick major labels
ax2.yaxis.set_major_locator(MultipleLocator(1.0))
ax2.yaxis.set_ticklabels([])  # turn off ytick major labels
# minor axes
ax2.xaxis.set_minor_locator(MultipleLocator(0.1))
ax2.xaxis.set_minor_formatter(FormatStrFormatter('%1.1f'))
ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
ax2.yaxis.set_minor_formatter(FormatStrFormatter('%1.1f'))

ax2.grid(b=True, which='major', linestyle='-')
ax2.grid(b=True, which='minor', linestyle=':')

ax2.fill([x_min_small, x_max_small, x_max_small, x_min_small],
        [y_min_small, y_min_small, y_max_small, y_max_small], bg_color)

ax2.plot(x1_small, y_green_lagrange_small, color='green', linestyle='-', linewidth=lw, label='Green-Lagrange', zorder=2)
ax2.plot(x1_small, y_engineering_small, color='blue', linestyle='--', linewidth=lw, label='engineering', zorder=4)
ax2.set_xlim(0.8, 1.2)
# ax2.set_ylim(-0.5, 0.5)

plt.show()

print_to_pdf = 0
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')
