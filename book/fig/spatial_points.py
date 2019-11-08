#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

NPTS = 10
OFFSET = 5
RADTODEG = 180.0/np.pi

x1 = [x for x in range(0, NPTS + 1, 1)]  # create one list 1 to 10
x1s = np.array(x1 * (NPTS + 1))  # create 10 such lists 1 to 10
y1s = np.array([[y] * (NPTS + 1) for y in range(0, NPTS + 1, 1)]).reshape(1, (NPTS + 1) * (NPTS + 1)).squeeze()


fig = plt.figure(figsize=(6, 6))  # 6 inches wide, 6 inches tall
# fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
# major axes
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
# minor axes
# ax.xaxis.set_minor_locator(MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(MultipleLocator(0.5))

# spatial grid
ax.plot(x1s - OFFSET, y1s - OFFSET, 'o', color='dimgray', alpha=0.5, label='spatial integer points')

# origin 
ax.plot(0, 0, 'o', color='black', label='origin = (0, 0, 0)')  # origin
ax.text(0.25, -0.25, r'$o$', ha='center', va='center')

# x-axis
# ax.plot([0, 1], [0, 0], '-', color='black', linewidth=2)  # x-axis leader
# ax.plot(1, 0, color='black', marker='>')  # x-axis arrowhead
ax.plot([0, 1], [0, 0], '-', marker='>', linewidth=2, color='red', markevery=[-1])  # x-axis
ax.text(1.4, 0, r'$\hat{\mathbf{e}}_1$', ha='center', va='center', backgroundcolor='white')

# y-axis
# ax.plot([0, 0], [0, 1], '-', color='black', linewidth=2)  # y-axis leader
# ax.plot(0, 1, color='black', marker='^')  # y-axis arrowhead
ax.plot([0, 0], [0, 1], '-', marker='^', linewidth=2, color='green', markevery=[-1])  # y-axis
ax.text(0, 1.4, r'$\hat{\mathbf{e}}_2$', ha='center', va='center', backgroundcolor='white')

# z-axis start
z_angle = np.linspace(-np.pi/2.0, np.pi)
z_radius = 0.5
ax.plot(z_radius * np.cos(z_angle), z_radius * np.sin(z_angle), color='blue')  # z-axis leader
ax.plot(-0.5, 0, marker='v', color='blue', zorder=4)  # z-axis arrowhead
ax.text(-0.5, -0.4, r'$\hat{\mathbf{e}}_3$', ha='center', va='center', backgroundcolor='white')

# spatial grid point
pt_color = 'purple'
px, py = 3, 4
ax.plot(px, py, 'o', color=pt_color, 
    label=r'spatial point {\em p} = (' + str(px) + ', ' + str(py) + ', 0)')
ax.plot([0, px], [0, py], color=pt_color, 
    label=r'spatial position vector {\bf \em r} $^{op} = (' + str(px) + ', ' + str(py) + ', 0)$', zorder=4)
o = 0.25
ax.text(px + o, py + o, r'$p$', ha='center', va='center')
angle = np.arctan(py / px)  # radians
angle_deg = angle * RADTODEG  # degrees
r_off = 0.25
dx = -r_off * np.cos(angle)
dy = -r_off * np.sin(angle)
ax.text(px + 4*dx, py + 2*dy, r'\bf{{\em r}} $^{op}$', ha='center', va='center', backgroundcolor='white', rotation=angle_deg)
ax.plot(px + dx, py + dy, marker=(3, 0, angle_deg - 90.0), markersize=8, color=pt_color, zorder=4)  # r-axis arrowhead

# ax.grid(which='both')
# ax.grid(b=True, which='major', linestyle='-')
ax.grid(b=True, which='major', linestyle=':')
# ax.grid(b=True, which='minor', linestyle=':')
ax.set_xlabel(r'spatial coordinate $x_1$')
ax.set_ylabel(r'spatial coordinate $x_2$')
a = 6
ax.set_xlim(-a, a)
ax.set_ylim(-a - 2, a + 1)
# ax.legend(loc='lower right', framealpha=1.0)
ax.legend(loc='lower right')

fig.tight_layout()
plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

