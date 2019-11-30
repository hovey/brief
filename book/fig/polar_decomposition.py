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
    the x-axis by distance shear_x (Length) to the current points (x, y).
    """
    x = X + shear_12 * Y
    y = Y
    return x, y

def stretch(X, Y, stretch_11):
    """ Given a list of reference points (X, Y), simple stretch them in 
    the x-axis by distance stretch_11 (factor l/L) to the current points (x, y).
    """
    x = stretch_11 * X
    y = Y
    return x, y

class BodyModel():
    def __init__(self):
        # origin
        self._X0, self._Y0 = 0, 0
        # perimeter
        r = 2  # radius
        theta = np.linspace(0.0, 2 * np.pi, 26)  # radians
        self._X = np.array(r * np.cos(theta))
        # Y = np.array([-r, 0, 0, 0, r])
        self._Y = np.array(r * np.sin(theta))

    def origin(self):
        return self._X0, self._Y0

    def perimeter(self):
        return self._X, self._Y

    @property
    def points(self):
        where = 0
        X = np.insert(self._X, where, self._X0, axis=0)
        Y = np.insert(self._Y, where, self._Y0, axis=0)
        return X, Y

    @points.setter  
    def points(self, value_x, value_y):
        self._X0 = value_x[0]
        self._Y0 = value_y[0]
        self._X = value_x[1:]
        self._Y = value_y[1:]


class BodyView():
    def __init__(self, points_body, axis):
        # origin 
        x0, y0 = points_body.origin()
        x, y = points_body.perimeter()

        axis.plot(x, y, 'o', color='magenta')  # boundary
        axis.plot([x0, x[0]], [y0, y[0]], 'o-', color='black')  # tracking line on original x-axis
        # axis.plot(x0, y0, 'o', color='black', label='origin = (0, 0, 0)')  # origin




def body():
    r = 3
    X = np.array([0, -r, 0, r, 0])
    Y = np.array([-r, 0, 0, 0, r])
    b_angle = np.linspace(0.0, 2 * np.pi, 10)
    body_object = dict({'origin_x': 0, 'origin_y': 0, 'boundary_x': X, 'boundary_y': Y})
    # return X, Y
    return body_object

def draw_body(axis, b):
    # origin 
    x = b['origin_x']
    y = b['origin_y']
    axis.plot(x, y, 'o', color='black', label='origin = (0, 0, 0)')  # origin

    x = b['boundary_x']
    y = b['boundary_y']
    axis.plot(x, y, 'o-', color='blue')  # boundary
    #axis.plot([x, x + 1], [y, y], '-', marker='o', linewidth=2, color='red', markevery=[-1], zorder=4)  # x-axis

fig = plt.figure(figsize=(6, 6))  # inches, (wide, tall)
ax = fig.add_subplot(1, 1, 1)

pb = BodyModel()
px, py = pb.points

gb = BodyView(pb, ax)

dx = -0
dy = -0
dr_deg = 0  # deg
RADTODEG = 180.0/np.pi
DEGTORAD = 1.0/RADTODEG
dr = dr_deg * DEGTORAD  # radian
shear_12 = 0.5 # Length units, shear in the X_1 direction

#region = body()
#draw_body(ax, region)

def draw(axis, ux=0, uy=0, ur=0, shear=0, t0=1, showlabels=0):
    MSIZE = 8  # marker size
    
    # body grid
#    NPTS = 7
#    row = [i for i in range(-3, 4, 1)]
#    NROWS = 3
    # X = np.array(row * NROWS)  # center, top, and bottom list
    # X = np.append(X, [-4.0, 4.0])  # the two end points, x coordinate
    # Y = np.array([[j] * NPTS for j in range(-1, 2, 1)]).reshape(1, NPTS * NROWS).squeeze()
    # Y = np.append(Y, [0, 0])  # the two end points, y coordinate
    r = 2
    X = np.array([0, -r, 0, r, 0])
    Y = np.array([-r, 0, 0, 0, r])
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, 'o', color='dimgray', alpha=0.5, label='body integer points')

    # origin 
    axis.plot(0 + ux, 0 + uy, 'o', color='black', label='origin = (0, 0, 0)')  # origin
#    ox = 0.25  # offset
#    oy = -0.25  # offset
#    X = 0 + ox
#    Y = 0 + oy
#    # x, y = rotate(X, Y, ur)
#    x, y = simple_shear(X, Y, shear)
#    if t0:
#        text = r'$O$'
#    else:
#        text = r'$o$'
#    axis.text(x + ux, y + uy, text, ha='center', va='center')
    
    # x-axis
    X = np.array([0, 1])
    Y = np.array([0, 0])
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    # axis.plot(x + ux, y + uy, '-', marker=(3, 1, ur * RADTODEG - 90.0), markersize=MSIZE, linewidth=2, color='red', markevery=[-1], zorder=4)  # x-axis
    axis.plot(x + ux, y + uy, '-', marker='o', linewidth=2, color='red', markevery=[-1], zorder=4)  # x-axis
#    ox = 0.5  # offset
#    oy = 0.0  # offset
#    X = X[-1] + ox
#    Y = Y[-1] + oy
#    # x, y = rotate(X, Y, ur)
#    x, y = simple_shear(X, Y, shear)
#    if t0:
#        text = r'${\mathbf{E}}_1$'
#    else:
#        text = r'${\mathbf{E}}_1$'
#    # axis.text(x + ux, y + uy, r'${\mathbf{E}}_1$', ha='center', va='center', backgroundcolor='white')
#    axis.text(x + ux, y + uy, text, ha='center', va='center', backgroundcolor='white')
    
    # y-axis
    X = np.array([0, 0])
    Y = np.array([0, 1])
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    # axis.plot(x + ux, y + uy, '-', marker=(3, 1, ur * RADTODEG), markersize=MSIZE, linewidth=2, color='green', markevery=[-1], zorder=4)  # y-axis
    axis.plot(x + ux, y + uy, '-', marker='o', linewidth=2, color='green', markevery=[-1], zorder=4)  # y-axis
#    ox = 0.0  # offset
#    oy = 0.5  # offset
#    X = X[-1] + ox
#    Y = Y[-1] + oy
    # x, y = rotate(X, Y, ur)
#    x, y = simple_shear(X, Y, shear)
#    if t0:
#        text = r'${\mathbf{E}}_2$'
#    else:
#        text = r'${\varphi_*[\mathbf{E}}_2]$'
#    axis.text(x + ux, y + uy, text, ha='center', va='center', backgroundcolor='white')
    
#    # z-axis start
#    z_angle = np.linspace(-np.pi/2.0, np.pi)
#    z_radius = 0.5
#    X = z_radius * np.cos(z_angle)
#    Y = z_radius * np.sin(z_angle)
#    # x, y = rotate(X, Y, ur)
#    no_shear = 0
#    x, y = simple_shear(X, Y, no_shear)  # don't shear the z-axis leader
#    axis.plot(x + ux, y + uy, color='blue', zorder=4)  # z-axis leader
#    # axis.plot(x[-1] + ux, y[-1] + uy, marker=(3, 1, ur * RADTODEG - 180.0), markersize=MSIZE, linewidth=2, color='blue', zorder=4)  # z-axis arrowhead
#    axis.plot(x[-1] + ux, y[-1] + uy, marker='o', linewidth=2, color='blue', zorder=4)  # z-axis arrowhead
#    ox = 0  # offset
#    oy = -0.5  # offset
#    X = X[-1] + ox
#    Y = Y[-1] + oy
#    # x, y = rotate(X, Y, ur)
#    x, y = simple_shear(X, Y, no_shear)
#    if t0:
#        text = r'${\mathbf{E}}_3$'
#    else:
#        text = r'${\mathbf{E}}_3$'
#    axis.text(x + ux, y + uy, text, ha='center', va='center', backgroundcolor='white')

    # body
    body_color = 'blue'
    
    p_color = 'purple'
    PX, PY = 2, 0  # circle coordinates, point P
    # px, py = rotate(PX, PY, ur)
    px, py = simple_shear(PX, PY, shear)
    axis.plot(px + ux, py + uy, 'o', color=p_color, label=r'body point {\em P} = (2, 0, 0)')  #  point P
    ox = 0.0  # offset
    oy = 0.25  # offset
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
    QX, QY = -2, 0  # circle coordinates, point Q
    # qx, qy = rotate(QX, QY, ur)
    qx, qy = simple_shear(QX, QY, shear)
    axis.plot(qx + ux, qy + uy, 'o', color=q_color, label=r'body point {\em Q} = (-2, 0, 0)')  #  point Q
    ox = 0.0  # offset
    oy = 0.25  # offset
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
    b_angle_p = np.linspace(-np.pi/2, np.pi/2, 10)
    # b_radius = 0.5
    b_radius_o = PX

#    X = b_radius * np.cos(b_angle) + PX
#    Y = b_radius * np.sin(b_angle) + PY
#    # x, y = rotate(X, Y, ur)
#    x, y = simple_shear(X, Y, shear)
#    axis.plot(x + ux, y + uy, color=body_color)  # P circle
    X = b_radius_o * np.cos(b_angle_p) + 0
    Y = b_radius_o * np.sin(b_angle_p) + 0
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, 'o-', color=body_color)  # P circle, outer
    p0x, p0y = x[0], y[0]
    p1x, p1y = x[-1], y[-1]

#    X = b_radius * np.cos(b_angle) + QX
#    Y = b_radius * np.sin(b_angle) + QY
#    # x, y = rotate(X, Y, ur)
#    x, y = simple_shear(X, Y, shear)
#    axis.plot(x + ux, y + uy, color=body_color)  # Q circle
    X = b_radius_o * np.cos(b_angle_q) + 0
    Y = b_radius_o * np.sin(b_angle_q) + 0
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    axis.plot(x + ux, y + uy, color=body_color)  # Q circle, outer
    q0x, q0y = x[0], y[0]
    q1x, q1y = x[-1], y[-1]
    
#     axis.plot([p1x + ux, q0x + ux], [p1y + uy, q0y + uy], color=body_color)  #  top bracket line
#     axis.plot([q1x + ux, p0x + ux], [q1y + uy, p0y + uy], color=body_color)  #  bottom bracket line



# x, y = stretch(X, Y, stretch_11=2)
# draw_region(ax, x, y)

draw(ax, ux=-3, uy=3, ur=dr)
draw(ax, ux=3, uy=-3, ur=dr, shear=shear_12, t0=False)


ax.axis('equal')
# major axes
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
# minor axes

ax.grid(b=True, which='major', linestyle=':')

ax.set_xlabel(r'reference configuration $X_1, x_1$')
ax.set_ylabel(r'reference configuration $X_2, x_2$')
a = 7
b = a
ax.set_xlim(-a, a)
ax.set_ylim(-b, b)
# ax.legend(loc='lower right', framealpha=1.0)
# ax1.legend(loc='lower right')

# fig.tight_layout()
plt.show()

print_to_pdf = 0
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

