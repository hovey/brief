#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker

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

def draw(axis, ux=0, uy=0, ur=0, shear=0, t0=1, showlabels=0, c='dimgray', ls='-'):
    MSIZE = 8  # marker size
    
    # body grid
    # NPTS = 7
    # row = [i for i in range(-3, 4, 1)]
    # NROWS = 3
    # X = np.array(row * NROWS)  # center, top, and bottom list
    X = np.array([0, 1, 1, 0, 0])
    # Y = np.array([[j] * NPTS for j in range(-1, 2, 1)]).reshape(1, NPTS * NROWS).squeeze()
    Y = np.array([0, 0, 1, 1, 0])
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        # c='dimgray'
        al=0.5
    else:
        # c='green'
        al=0.9
    axis.plot(x + ux, y + uy, '-o', color=c, alpha=al, linestyle=ls, label='body integer points')  # body outline

    # origin 
    axis.plot(0 + ux, 0 + uy, 'o', color='black', label='origin = (0, 0, 0)')  # origin
    ox = 0.25  # offset
    oy = -0.25  # offset
    X = 0 + ox
    Y = 0 + oy
    # x, y = rotate(X, Y, ur)
    x, y = simple_shear(X, Y, shear)
    if t0:
        text = r'$O, o$'
        axis.text(x + ux, y + uy, text, ha='center', va='center')
    
    # body
    body_color = 'black'
    axis.plot(x + ux, y + uy, color=body_color)  # body outline

    if t0:
        s = 0.90  # scale
        hairline_offset_y = 0.1
        epsx, epsy = 0.125, 0.25 + hairline_offset_y
        x, y = simple_shear(np.array([0, 0, 0.25])*s, np.array([0, 0.5, 0.5])*s, shear)
        axis.plot(x + epsx, y + epsy, lw=0.5, color='green')
        axis.text(0.125, 0.5, '1', color='green', ha='right', va='center')
        axis.text(0.25, 0.85, r'$a$', color='green', ha='center')


fig = plt.figure(figsize=(6, 3))  # inches, (wide, tall)
# fig = plt.figure()  # inches, (wide, tall)
# fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

dx = -0
dy = -0
dr_deg = 0  # deg
RADTODEG = 180.0/np.pi
DEGTORAD = 1.0/RADTODEG
dr = dr_deg * DEGTORAD  # radian
draw(ax1, ux=dx, uy=dy, ur=dr)

shear_12 = 0.5 # Length units, shear in the X_1 direction
draw(ax1, ux=dx, uy=dy, ur=dr, shear=shear_12, t0=False, c='green', ls=':')

shear_12 = 1.0 # Length units, shear in the X_1 direction
draw(ax1, ux=dx, uy=dy, ur=dr, shear=shear_12, t0=False, c='red', ls='--')

ax1.axis('equal')
# ax2.axis('equal')
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
ax1.set_xlabel(r'configuration $X_1, x_1$')
ax1.set_ylabel(r'configuration $X_2, x_2$')

x_min = 0
x_max = 10
epsx, epsy = 0.4, np.pi/16
x = np.linspace(x_min, x_max)
y = np.arctan(x)
# ax2.plot(x, y/np.pi, linewidth=2, color='blue')
ax2.plot(x, y, linewidth=2, color='blue')
ax2.text(x_max - epsx, np.pi/2 + epsy/4, r'$\gamma \mapsto \frac{\pi}{2}$', ha='right', backgroundcolor='white')
ax2.plot([x_min, x_max], np.pi/2*np.array([1, 1]), lw=2, alpha=0.5, color='black', linestyle='--', zorder=4)

ax2.plot(0, 0, 'o', color='dimgray', alpha=0.5, zorder=4)
ax2.text(0 + epsx, 0 - epsy, r'$(0, 0)$', backgroundcolor='white')

ax2.plot(0.5, 0.46, 'o', color='green', alpha=0.9, zorder=4)
ax2.text(0.50 + epsx, 0.46 - epsy, r'$(0.50, 0.46)$', backgroundcolor='white')

ax2.plot(1, np.pi/4, 'o', color='red', alpha=0.9, zorder=4)
ax2.text(1 + epsx, np.pi/4 - epsy, r'$(1, \frac{\pi}{4})$', backgroundcolor='white')

ax2.set_xlabel(r'non-dimensional distance $a\;[l/L]$')
ax2.set_ylabel(r'$\gamma = \arctan(a)$ [rad]')
# ax2.xaxis.xticks([1, 5, 10])
# https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-locators.html
# ax2.xaxis.set_major_locator(ticker.FixedLocator([0, 5, 10]))
ax2.set_xticks([0, 5, 10])
# ax2.set_xticklabels(['a', 'b', 'c'])
# ax2.xticks([0, 5, 10], ['a', 'b', 'c'])
# ax2.yaxis.set_major_locator(MultipleLocator(np.pi/4))
ax2.set_yticks([0, np.pi/4, np.pi/2])
ax2.set_yticklabels(['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$'])
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%g $\pi/4$'))

ax1.set_xlim(-epsx, 2 + epsx)
# ax1.set_ylim(ax1.get_xlim())
ax2.set_xlim(0 - epsx, x_max + epsx)
eps = np.pi/8
ax2.set_ylim(0*np.pi/4 - eps, np.pi/2 + eps)
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

