#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
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
edgey = 4.5
#fig = plt.figure(figsize=(6, 6))  # inches, (wide, tall)
fig = plt.figure(figsize=(edgex, edgey))  # inches, (wide, tall)
ax = fig.add_subplot(1, 1, 1)

def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
        ha='center', va='center_baseline', weight='bold', color='black')

c = 4  # notational origin (center) for each of the four plots
#m = c + 3  # motional origin plus margin
inner = 3  # inner margin position

ap = dict(arrowstyle='<-') # arrow properites
ax.annotate('', xy=(inner, c), xytext=(-inner, c), arrowprops=ap)
text(0, c, 'pull back $\\varphi_*^{-1}$')
# https://tex.stackexchange.com/questions/7669/bfseries-is-to-textbf-as-what-is-to-textsf/7670

ap = dict(arrowstyle='->') # arrow properites
ax.annotate('', xy=(-c, -inner), xytext=(-c, inner), arrowprops=ap)
rscale = 0.9
text(-c, 0, 'time derivative $\\frac{\partial}{\partial t}$')

ax.annotate('', xy=(inner, -c), xytext=(-inner, -c), arrowprops=ap)
text(0, -c, 'push forward $\\varphi_*$')

ax.annotate('', xy=(c, -inner), xytext=(c, inner), arrowprops=ap)
text(c, 0, 'Lie derivative $\\mathcal L$')

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

#text(-edge + 1, edge - 1, '(b)')
#text(edge - 1, edge - 1, '(a)')
#text(-edge + 1, -edge + 1, '(c)')
#text(edge - 1, -edge + 1, '(d)')

text( c,  c, '\sffamily \\bfseries e')
text(-c,  c, '\sffamily \\bfseries E') # no white background
text(-c, -c, '$\\frac{\partial}{\partial t}$ \sffamily \\bfseries E')
text( c, -c, '\sffamily \\bfseries d')


# fig.tight_layout()
plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

