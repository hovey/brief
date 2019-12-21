#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator
from abc import ABC

latex = 1
if latex:
    #rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
    rc('text', usetex=True)
    rc('font', family='serif')
    # matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
    rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

# horizontal and vertical dividing lines
edgex = 6
edgey = 3
#fig = plt.figure(figsize=(6, 6))  # inches, (wide, tall)
fig = plt.figure(figsize=(edgex, edgey))  # inches, (wide, tall)
ax = fig.add_subplot(1, 1, 1)

def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
        ha='center', va='center_baseline', weight='bold', color='black')

# https://tex.stackexchange.com/questions/7669/bfseries-is-to-textbf-as-what-is-to-textsf/7670
ap = dict(arrowstyle='->') # arrow properties

x, y = (4, 1)

ax.annotate('', xy=(-x, -y), xytext=(-x, y), arrowprops=ap)
text(-x, 0, 'time derivative $\\frac{\partial}{\partial t}$')

ax.annotate('', xy=(x, -y), xytext=(x, y), arrowprops=ap)
text(x, 0, 'Lie derivative $\\mathcal L$')

x, y = (3, 2)

ax.annotate('', xy=(-x, y), xytext=(x, y), arrowprops=ap)
text(0, y, 'pull back $\\varphi_*^{-1}$')

ax.annotate('', xy=(x, -y), xytext=(-x, -y), arrowprops=ap)
text(0, -y, 'push forward $\\varphi_*$')

ax.axis('equal')

# major axes
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
plt.axis('off') # turn off grid and axes

# minor axes
# no operations

#ax.set_xlabel(r'$X_1, x_1$')
#ax.set_ylabel(r'$X_2, x_2$')
ax.set_xlim(-edgex, edgex)
ax.set_ylim(-edgey, edgey)

#ax.set_xticklabels(['', '', -3, -2, -1, 0, 1, 2, 3, '', -3, -2, -1, 0, 1, 2, 3])
#ax.set_yticklabels(['', '', -3, -2, -1, 0, 1, 2, 3, '', -3, -2, -1, 0, 1, 2, 3])

x, y = (4, 2)
r = 0.75
ax.add_patch(mpatches.Circle((x, y), radius=r, facecolor='lightgray', edgecolor='black')) # e
ax.text(x, y, '\sffamily \\bfseries e', ha='center', va='center')

ax.add_patch(mpatches.Circle((-x, y), radius=r, facecolor='lightgray', edgecolor='black')) # E
ax.text(-x, y, '\sffamily \\bfseries E', ha='center', va='center') # no white background

ax.add_patch(mpatches.Circle((x, -y), radius=r, facecolor='lightgray', edgecolor='black')) # d
nudge_y = 0.0625
ax.text(-x, -(y + nudge_y), '$\\frac{\partial}{\partial t}$ \sffamily \\bfseries E', ha='center', va='center')

ax.add_patch(mpatches.Circle((-x, -y), radius=r, facecolor='lightgray', edgecolor='black')) # Edot
ax.text( x, -y, '\sffamily \\bfseries d', ha='center', va='center')


# fig.tight_layout()
plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

