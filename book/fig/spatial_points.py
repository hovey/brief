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
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))

ax.plot(x1s - OFFSET, y1s - OFFSET, 'o', color='cornflowerblue')
ax.plot([0, 3], [0, 4], 'o--', color='blue', label=r'spatial location $(x_1, x_2, x_3) = (3, 4, 0)$')
ax.plot([0, 1], [0, 0], '-', color='black', linewidth=2)  # x-axis leader
ax.plot(1, 0, '-', color='black', marker='>', linewidth=2)  # x-axis arrowhead
ax.plot([0, 0], [0, 1], '-', color='black', linewidth=2)  # y-axis leader
ax.plot(0, 1, '-', color='black', marker='^', linewidth=2)  # y-axis arrowhead
ax.plot(0, 0, 'o', color='black', label='origin = (0, 0, 0)')
ax.text(1.5, 0, r'$\hat{\mathbf{e}}_1$', ha='center', va='center', backgroundcolor='white')
ax.text(0, 1.5, r'$\hat{\mathbf{e}}_2$', ha='center', va='center', backgroundcolor='white')
# ax.grid(which='both')
ax.grid(b=True, which='major', linestyle='-')
ax.grid(b=True, which='minor', linestyle=':')
ax.set_xlabel(r'spatial coordinate $x_1$')
ax.set_ylabel(r'spatial coordinate $x_2$')
a = 9
ax.set_xlim(-a, a)
ax.set_ylim(-a, a+1)
ax.legend(loc='upper right')

fig.tight_layout()
plt.show()

print_to_pdf = 0
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')
