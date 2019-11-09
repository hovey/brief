#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)


def rotate(X, Y, R):
    """ Given list of reference points (X, Y), rotate them about the 
    z-axis by angle R (radians) to the current points (x, y).
    """
    x = np.cos(R) * X - np.sin(R) * Y
    y = np.sin(R) * X + np.cos(R) * Y
    return x, y

def simple_shear(X, Y, shear_12):
    """ Given a list of reference points (X, Y), simple shear them in 
    the x-axis by distance shear_x (Lenght) to the current points (x, y).
    """
    x = X + shear_12 * Y
    y = Y
    return x, y

def draw(axis, ux=0, uy=0, ur=0, shear=0, t0=1, showlabels=0):
    MSIZE = 8  # marker size
    
    # body grid
    NPTS = 7
    row = [i for i in range(-3, 4, 1)]
    NROWS = 3
    X = np.array(row * NROWS)  # center, top, and bottom list
    X = np.append(X, [-4.0, 4.0])  # the two end points, x coordinate
    Y = np.array([[j] * NPTS for j in range(-1, 2, 1)]).reshape(1, NPTS * NROWS).squeeze()
    Y = np.append(Y, [0, 0])  # the two end points, y coordinate
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, 'o', color='dimgray', alpha=0.5, label='body integer points')

    # origin 
    axis.plot(0 + ux, 0 + uy, 'o', color='black', label='origin = (0, 0, 0)')  # origin
    ox = 0.25  # offset
    oy = -0.25  # offset
    X = 0 + ox
    Y = 0 + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'$O$'
    else:
        text = r'$o$'
    axis.text(x + ux, y + uy, text, ha='center', va='center')
    
    # x-axis
    X = np.array([0, 1])
    Y = np.array([0, 0])
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    # axis.plot(x + ux, y + uy, '-', marker=(3, 1, ur * RADTODEG - 90.0), markersize=MSIZE, linewidth=2, color='red', markevery=[-1], zorder=4)  # x-axis
    axis.plot(x + ux, y + uy, '-', marker='o', linewidth=2, color='red', markevery=[-1], zorder=4)  # x-axis
    ox = 0.5  # offset
    oy = 0.0  # offset
    X = X[-1] + ox
    Y = Y[-1] + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'${\mathbf{E}}_1$'
    else:
        text = r'${\mathbf{e}}_1$'
    # axis.text(x + ux, y + uy, r'${\mathbf{E}}_1$', ha='center', va='center', backgroundcolor='white')
    axis.text(x + ux, y + uy, text, ha='center', va='center', backgroundcolor='white')
    
    # y-axis
    X = np.array([0, 0])
    Y = np.array([0, 1])
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    # axis.plot(x + ux, y + uy, '-', marker=(3, 1, ur * RADTODEG), markersize=MSIZE, linewidth=2, color='green', markevery=[-1], zorder=4)  # y-axis
    axis.plot(x + ux, y + uy, '-', marker='o', linewidth=2, color='green', markevery=[-1], zorder=4)  # y-axis
    ox = 0.0  # offset
    oy = 0.5  # offset
    X = X[-1] + ox
    Y = Y[-1] + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'${\mathbf{E}}_2$'
    else:
        text = r'${\mathbf{e}}_2$'
    axis.text(x + ux, y + uy, text, ha='center', va='center', backgroundcolor='white')
    
    # z-axis start
    z_angle = np.linspace(-np.pi/2.0, np.pi)
    z_radius = 0.5
    X = z_radius * np.cos(z_angle)
    Y = z_radius * np.sin(z_angle)
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, color='blue', zorder=4)  # z-axis leader
    # axis.plot(x[-1] + ux, y[-1] + uy, marker=(3, 1, ur * RADTODEG - 180.0), markersize=MSIZE, linewidth=2, color='blue', zorder=4)  # z-axis arrowhead
    axis.plot(x[-1] + ux, y[-1] + uy, marker='o', linewidth=2, color='blue', zorder=4)  # z-axis arrowhead
    ox = 0  # offset
    oy = -0.5  # offset
    X = X[-1] + ox
    Y = Y[-1] + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'${\mathbf{E}}_3$'
    else:
        text = r'${\mathbf{e}}_3$'
    axis.text(x + ux, y + uy, text, ha='center', va='center', backgroundcolor='white')

    # body
    body_color = 'black'
    
    p_color = 'purple'
    PX, PY = 3, 0  # circle coordinates, point P
    # px, py = rotate(PX, PY, ur)
    px, py = simple_shear(PX, PY, shear)
    axis.plot(px + ux, py + uy, 'o', color=p_color, label=r'body point {\em P} = (3, 0, 0)')  #  point P
    ox = 0.25  # offset
    oy = -0.25  # offset
    X = PX + ox
    Y = PY + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'$P$'
    else:
        text = r'$p$'
    axis.text(x + ux, y  + uy, text, ha='center', va='center')
    
    q_color = 'magenta'
    QX, QY = -3, 0  # circle coordinates, point Q
    # qx, qy = rotate(QX, QY, ur)
    qx, qy = simple_shear(QX, QY, shear)
    axis.plot(qx + ux, qy + uy, 'o', color=q_color, label=r'body point {\em Q} = (-3, 0, 0)')  #  point Q
    ox = 0.22  # offset
    oy = -0.25  # offset
    X = QX + ox
    Y = QY + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'$Q$'
    else:
        text = r'$q$'
    axis.text(x + ux, y + uy, text, ha='center', va='center')

    b_angle = np.linspace(0.0, 2 * np.pi)
    b_angle_q = np.linspace(np.pi/2, 3*np.pi/2)
    b_angle_p = np.linspace(-np.pi/2, np.pi/2)
    b_radius = 0.5
    b_radius_o = 1.0

    X = b_radius * np.cos(b_angle) + PX
    Y = b_radius * np.sin(b_angle) + PY
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, color=body_color)  # P circle
    X = b_radius_o * np.cos(b_angle_p) + PX
    Y = b_radius_o * np.sin(b_angle_p) + PY
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, color=body_color)  # P circle, outer
    p0x, p0y = x[0], y[0]
    p1x, p1y = x[-1], y[-1]

    X = b_radius * np.cos(b_angle) + QX
    Y = b_radius * np.sin(b_angle) + QY
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, color=body_color)  # Q circle
    X = b_radius_o * np.cos(b_angle_q) + QX
    Y = b_radius_o * np.sin(b_angle_q) + QY
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, color=body_color)  # Q circle, outer
    q0x, q0y = x[0], y[0]
    q1x, q1y = x[-1], y[-1]
    
    axis.plot([p1x + ux, q0x + ux], [p1y + uy, q0y + uy], color=body_color)  #  top bracket line
    axis.plot([q1x + ux, p0x + ux], [q1y + uy, p0y + uy], color=body_color)  #  bottom bracket line


fig = plt.figure(figsize=(6, 6))  # inches, (wide, tall)
# fig = plt.figure()  # inches, (wide, tall)
# fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

dx = -0
dy = -0
dr_deg = 0  # deg
RADTODEG = 180.0/np.pi
DEGTORAD = 1.0/RADTODEG
dr = dr_deg * DEGTORAD  # radian
shear_12 = 0.5 # Length units, shear in the X_1 direction
draw(ax1, ux=dx, uy=dy, ur=dr)
draw(ax2, ux=dx, uy=dy, ur=dr, shear=shear_12, t0=False)

ax1.axis('equal')
ax2.axis('equal')
# major axes
ax1.xaxis.set_major_locator(MultipleLocator(1.0))
ax1.yaxis.set_major_locator(MultipleLocator(1.0))
ax2.xaxis.set_major_locator(MultipleLocator(1.0))
ax2.yaxis.set_major_locator(MultipleLocator(1.0))
# minor axes
# ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(MultipleLocator(0.5))

# ax.grid(which='both')
# ax.grid(b=True, which='major', linestyle='-')
ax1.grid(b=True, which='major', linestyle=':')
ax2.grid(b=True, which='major', linestyle=':')
# ax.grid(b=True, which='minor', linestyle=':')
ax1.set_xlabel(r'reference configuration $X_1, x_1$')
ax1.set_ylabel(r'reference configuration $X_2, x_2$')
ax2.set_xlabel(r'current configuration $x_1$')
ax2.set_ylabel(r'current configuration $x_2$')
a = 5.9
b = 2.9
ax1.set_xlim(-a, a)
ax1.set_ylim(-b, b)
ax2.set_xlim(ax1.get_xlim())
ax2.set_ylim(ax1.get_ylim())
# ax.legend(loc='lower right', framealpha=1.0)
# ax1.legend(loc='lower right')

# fig.tight_layout()
plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

