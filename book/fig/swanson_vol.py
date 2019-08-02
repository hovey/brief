#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

lw = 2  # line width

# num_sides = 6  # number of sides on dice
x1 = np.arange(0, 3, 0.01)   # plot limits to be [ 0, 3]
x2 = np.arange(0.01, 3, 0.01)   # plot limits to be [ 0.1, 3]
# first compressible neo-Hookean volumetric term, normalized by K/2.
y1 = (x1 - 1.0)**2  # plot limits to be [-2, 2]
y2 = 0.5*(x2**2 - 1.0) - 1.0 * np.log(x2)  # np.log is the natural log, s.t. log(exp(x)) = x
# y2a = 0.5*(x1**2 - 1.0)  # np.log is the natural log, s.t. log(exp(x)) = x
# y2b = -1.0 * np.log(x2)  # np.log is the natural log, s.t. log(exp(x)) = x
y3 = 2*(x2 * np.log(x2) - x2 + 1)  # volumetric term of Swanson elastic

fig = plt.figure(figsize=(6, 6))  # 6 inches wide, 6 inches tall
# fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
# major axes
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
# minor axes
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

ax.plot(x1, y1, color='red', linestyle='--', linewidth=lw, label='$(J-1)^2$ small strain Neo-Hookean', zorder=4)
ax.plot(x2, y2, color='blue', linewidth=lw, label='$(J^2-1)/2 - \ln(J)$ finite strain Neo-Hookean', zorder=3)
# ax.plot(x1, y2a, color='green', linestyle=':', linewidth=lw, label='$(J^2-1)/2$', zorder=2)
# ax.plot(x2, y2b, color='magenta', linestyle='-.', linewidth=lw, label='$-\ln(J)$', zorder=1)
ax.plot(x2, y3, color='black', linestyle=':', linewidth=lw+1, label='$2 (J \ln(J) - J + 1)$ Swanson', zorder=1)
# ax.plot(3.5, 1, 'o', color='red', markersize=12, alpha=0.5, label='roll average')
# ax.grid(which='both')
ax.grid(b=True, which='major', linestyle='-')
ax.grid(b=True, which='minor', linestyle=':')
ax.set_xlabel('Jacobian $J$')
ax.set_ylabel('volumetric strain energy $W_{\mbox{vol}}(J)$ normalized by $K/2$')
ax.set_xlim(0, 3)
ax.set_ylim(-1, 2)
ax.legend(loc='lower right')


def text_elements(x, y, text, textcolor='blue'):  # helper function
    ax.text(x, y, text, backgroundcolor='white',
            ha='center', va='center', weight='normal', color=textcolor)


fig.tight_layout()
plt.show()

print_to_pdf = 0
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')
