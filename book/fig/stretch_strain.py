#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)


latex = 1
if latex:
#rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
    from matplotlib import rc
    rc('text', usetex=True)
    rc('font', family='serif')

lw = 2  # line width

x1 = np.arange(0, 3, 0.01)   # plot limits to be [ 0, 3]
x2 = np.arange(0.01, 3, 0.01)   # plot limits to be [ 0.1, 3]

x_min_small = 0.8
x_max_small = 1.2
y_min_small = -0.2
y_max_small = 0.2

#x1_small = np.arange(x_min_small, x_max_small, 0.01)   # plot limits to be [ 0, 3]
x1_small = np.linspace(x_min_small, x_max_small)   # plot limits to be [ 0, 3]

y_green_lagrange = 0.5*(x1**2 - 1.0)
y_engineering = x1 - 1.0
y_log = np.log(x2)
y_true = 1.0 - (1.0 / x2)
y_almansi_euler = 0.5*(1 - (1.0/x2)**2)

y_green_lagrange_small = 0.5*(x1_small**2 - 1.0)
y_engineering_small = x1_small - 1.0
y_log_small = np.log(x1_small)
y_true_small = 1.0 - (1.0 / x1_small)
y_almansi_euler_small = 0.5*(1 - (1.0/x1_small)**2)

# relative y-axis plot
yrel = y_log_small
yrel_green_lagrange_small = 0.5*(x1_small**2 - 1.0) - yrel
yrel_engineering_small = x1_small - 1.0 - yrel
yrel_log_small = np.log(x1_small) - yrel
yrel_true_small = 1.0 - (1.0 / x1_small) - yrel
yrel_almansi_euler_small = 0.5*(1 - (1.0/x1_small)**2) - yrel


fig = plt.figure(figsize=(6, 8))  # 6 inches wide, 8 inches tall
#fig = plt.figure(figsize=(9, 12))  
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
ax_x0, ax_x1 = 0, 3
ax_y0, ax_y1 = -2, 2
# axes lines
ax.plot([ax_x0, ax_x1], [0, 0], color='dimgray', linewidth=1.0)  # x-axis
ax.plot([1, 1], [ax_y0, ax_y1], color='dimgray', linewidth=1.0)  # y-axis
# major axes
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
# minor axes
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

bg_color = 'lightyellow'  # background color for inset
bg_line_color = 'gray'  # background line color for inset
bg_x = [x_min_small, x_max_small, x_max_small, x_min_small, x_min_small]
bg_y = [y_min_small, y_min_small, y_max_small, y_max_small, y_min_small]

ax.fill(bg_x, bg_y, bg_color)
ax.plot(bg_x, bg_y, color=bg_line_color, linestyle='-', linewidth=1.0)
ax.plot(x1, y_green_lagrange, color='green', linestyle='-', linewidth=lw, label='Green-Lagrange', zorder=2)
ax.plot(x1, y_engineering, color='blue', linestyle='--', linewidth=lw, label='engineering', zorder=4)
ax.plot(x2, y_log, color='red', linestyle='-', linewidth=lw+1, label='log (Hencky, natural)', zorder=2)
ax.plot(x2, y_true, color='cyan', linestyle='-.', linewidth=lw, label='true', zorder=3)
ax.plot(x2, y_almansi_euler, color='magenta', linestyle=':', linewidth=lw, label='Almansi-Euler', zorder=2)

ax.grid(b=True, which='major', linestyle='-')
# ax.grid(b=False, which='minor', linestyle=':', linewidth=0.25)

xlabel = 'stretch $\lambda = \ell / L$'
ylabel = 'strain $f(\lambda)$'
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
# ax.legend(loc='lower right')
ax.legend(loc='upper left')
ax.set_xlim(ax_x0, ax_x1)
ax.set_ylim(ax_y0, ax_y1)

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

# -------------
# second figure
# -------------

# fig = plt.figure(figsize=(6, 6))  # 6 inches wide, 6 inches tall
# fig = plt.figure(figsize=(6, 12))  # 6 inches wide, 6 inches tall
#fig = plt.figure(figsize=(10, 5))
fig = plt.figure(figsize=(5, 10))

# -------------
# right-subplot
# -------------

#ax = fig.add_subplot(1, 2, 2)
ax = fig.add_subplot(2, 1, 2)
ax_x0, ax_x1 = 0.80, 1.20  # overwrite
ax_y0, ax_y1 = -0.20, 0.20  # overwrite
ylabel_rel = 'strain difference $f(\lambda) - \ln \lambda$'
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel_rel)

ax.axis('equal')
# major axes
ax.xaxis.set_major_locator(MultipleLocator(1.0))
# ax.xaxis.set_ticklabels([])  # turn off xtick major labels
ax.yaxis.set_major_locator(MultipleLocator(1.0))
# ax.yaxis.set_ticklabels([])  # turn off ytick major labels
# minor axes
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_minor_formatter(FormatStrFormatter('%1.2f'))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_formatter(FormatStrFormatter('%1.2f'))

ax.grid(b=True, which='major', linestyle='-', linewidth=1.0, color='dimgray')
ax.grid(b=True, which='minor', linestyle=':')

ax.fill([x_min_small, x_max_small, x_max_small, x_min_small],
        [y_min_small, y_min_small, y_max_small, y_max_small], bg_color)
ax.plot(bg_x, bg_y, color=bg_line_color, linestyle='-', linewidth=1.0)

ax.plot(x1_small, yrel_green_lagrange_small, color='green', linestyle='-', linewidth=lw, label='Green-Lagrange', zorder=2)
ax.plot(x1_small, yrel_engineering_small, color='blue', linestyle='--', linewidth=lw, label='engineering', zorder=4)
ax.plot(x1_small, yrel_log_small, color='red', linestyle='-', linewidth=lw+1, label='log (Hencky, natural)', zorder=2)
ax.plot(x1_small, yrel_true_small, color='cyan', linestyle='-.', linewidth=lw, label='true', zorder=3)
ax.plot(x1_small, yrel_almansi_euler_small, color='magenta', linestyle=':', linewidth=lw, label='Almansi-Euler', zorder=2)

# ax.legend(loc='upper center')
ax.set_xlim(ax_x0, ax_x1)
ax.set_ylim(ax_y0, ax_y1)

# ------------
# left-subplot
# ------------
#ax2 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(2, 1, 1)
# ax.legend(loc='lower right')
ax2.axis('equal')
# major axes
ax2.xaxis.set_major_locator(MultipleLocator(1.0))
# ax2.xaxis.set_ticklabels([])  # turn off xtick major labels
ax2.yaxis.set_major_locator(MultipleLocator(1.0))
# ax2.yaxis.set_ticklabels([])  # turn off ytick major labels
# minor axes
ax2.xaxis.set_minor_locator(MultipleLocator(0.05))
ax2.xaxis.set_minor_formatter(FormatStrFormatter('%1.2f'))
ax2.yaxis.set_minor_locator(MultipleLocator(0.05))
ax2.yaxis.set_minor_formatter(FormatStrFormatter('%1.2f'))

ax2.grid(b=True, which='major', linestyle='-', linewidth=1.0, color='dimgray')
ax2.grid(b=True, which='minor', linestyle=':')

ax2.fill([x_min_small, x_max_small, x_max_small, x_min_small],
        [y_min_small, y_min_small, y_max_small, y_max_small], bg_color)
ax2.plot(bg_x, bg_y, color=bg_line_color, linestyle='-', linewidth=1.0)

ax2.plot(x1_small, y_green_lagrange_small, color='green', linestyle='-', linewidth=lw, label='Green-Lagrange', zorder=2)
ax2.plot(x1_small, y_engineering_small, color='blue', linestyle='--', linewidth=lw, label='engineering', zorder=4)
ax2.plot(x1_small, y_log_small, color='red', linestyle='-', linewidth=lw+1, label='log (Hencky, natural)', zorder=2)
ax2.plot(x1_small, y_true_small, color='cyan', linestyle='-.', linewidth=lw, label='true', zorder=3)
ax2.plot(x1_small, y_almansi_euler_small, color='magenta', linestyle=':', linewidth=lw, label='Almansi-Euler', zorder=2)

ax2.set_xlabel(xlabel)
ax2.set_ylabel(ylabel)
ax2.legend(loc='lower right')
ax2.set_xlim(ax_x0, ax_x1)
ax2.set_ylim(ax_y0, ax_y1)
#ax2.margins(x=-0.45, y=-0.45)

# https://matplotib.org/3.1.1/tutorials/intermediate/tight_layout_guide.html
plt.tight_layout()  # attempt to prevent subplot overlap

plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0] + '_rel'
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

