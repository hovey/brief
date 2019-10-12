#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

NPTS = 7
OFFSET = 0
RADTODEG = 180.0/np.pi

x1 = [x for x in range(-3, 4, 1)]
NROWS = 3
x1s = np.array(x1 * NROWS)  # center, top, and bottom list
x1s = np.append(x1s, [-4.0, 4.0])  # the two end points, x coordinate
y1s = np.array([[y] * NPTS for y in range(-1, 2, 1)]).reshape(1, NPTS * NROWS).squeeze()
y1s = np.append(y1s, [0, 0])  # the two end points, y coordinate

fig = plt.figure(figsize=(6, 3))  # inches, (wide, tall)
# fig = plt.figure()  # inches, (wide, tall)
# fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
# major axes
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
# minor axes
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))

# spatial grid
ax.plot(x1s + OFFSET, y1s + OFFSET, 'o', color='dimgray', alpha=0.5, label='body integer points')

# origin 
ax.plot(0, 0, 'o', color='black', label='origin = (0, 0, 0)')  # origin
ax.text(0.25, -0.25, r'$O$', ha='center', va='center')

# x-axis
ax.plot([0, 1], [0, 0], '-', marker='>', linewidth=2, color='red', markevery=[-1])  # x-axis
ax.text(1.5, 0, r'$\hat{\mathbf{b}}_1$', ha='center', va='center', backgroundcolor='white')

# y-axis
ax.plot([0, 0], [0, 1], '-', marker='^', linewidth=2, color='green', markevery=[-1])  # y-axis
ax.text(0, 1.5, r'$\hat{\mathbf{b}}_2$', ha='center', va='center', backgroundcolor='white')

# z-axis start
z_angle = np.linspace(-np.pi/2.0, np.pi)
z_radius = 0.5
ax.plot(z_radius * np.cos(z_angle), z_radius * np.sin(z_angle), color='blue')  # z-axis leader
ax.plot(-0.5, 0, marker='v', color='blue', zorder=4)  # z-axis arrowhead
ax.text(-0.5, -0.4, r'$\hat{\mathbf{b}}_3$', ha='center', va='center', backgroundcolor='white')

# body
body_color = 'black'
b_angle = np.linspace(0.0, 2 * np.pi)
b_angle_q = np.linspace(np.pi/2, 3*np.pi/2)
b_angle_p = np.linspace(-np.pi/2, np.pi/2)
b_radius = 0.5
b_radius_o = 1.0

px, py = 3, 0  # circle coordinates, point P
p_color = 'purple'
ax.plot(px, py, 'o', color=p_color, label=r'body point {\em P} = (3, 0, 0)')  #  point P
ax.text(px + 0.25, py - 0.25, r'$P$', ha='center', va='center')

qx, qy = -3, 0  # circle coordinates, point Q
q_color = 'magenta'
ax.plot(qx, qy, 'o', color=q_color, label=r'body point {\em Q} = (-3, 0, 0)')  #  point Q
ax.text(qx + 0.22, qy - 0.25, r'$Q$', ha='center', va='center')

ax.plot(b_radius * np.cos(b_angle) + px, b_radius * np.sin(b_angle) + py, color=body_color)  # P circle
ax.plot(b_radius * np.cos(b_angle) + qx, b_radius * np.sin(b_angle) + qy, color=body_color)  # Q circle

ax.plot(b_radius_o * np.cos(b_angle_p) + px, b_radius_o * np.sin(b_angle_p) + py, color=body_color)  # P circle, outer
ax.plot(b_radius_o * np.cos(b_angle_q) + qx, b_radius_o * np.sin(b_angle_q) + qy, color=body_color)  # R circle, outer

ax.plot([px, qx], [py + b_radius_o, qy + b_radius_o], color=body_color)  #  top bracket line
ax.plot([px, qx], [py - b_radius_o, qy - b_radius_o], color=body_color)  #  bottom bracket line

# ax.grid(which='both')
ax.grid(b=True, which='major', linestyle='-')
ax.grid(b=True, which='minor', linestyle=':')
ax.set_xlabel(r'body coordinate $X_1$')
ax.set_ylabel(r'body coordinate $X_2$')
a = 5.9
b = 2.9
ax.set_xlim(-a, a)
ax.set_ylim(-b - 2, b)
# ax.legend(loc='lower right', framealpha=1.0)
ax.legend(loc='lower right')

# fig.tight_layout()
plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')
