#!/usr/bin/env python3
# dice_moment.py
import numpy as np
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

lw = 1 # line width for leader lines

num_sides = 6  # number of sides on dice
x = np.linspace(1, num_sides, num_sides)
y = np.ones(6)  #  normalized equal probability

fig = plt.figure(figsize=(8, 4))  # 8 inches wide, 4 inches tall
# fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 's', color='blue', label='roll outcome')
ax.plot(3.5, 1, 'o', color='red', markersize=12, alpha=0.5, label='roll average')
ax.grid()
ax.set_xlabel('roll outcome')
ax.set_ylabel('normalized probability of outcome')
ax.set_ylim(-0.15, 1.5)
ax.legend(loc='upper right')

# helper functions
def text_elements(x, y, text, textcolor='blue'):
    ax.text(x, y, text, backgroundcolor='white',
            ha='center', va='center', weight='normal', color=textcolor)

h_lines_elevation = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
dy = 0.03
dy_array = dy * np.ones(num_sides)  # delta y for leader lines

# left-hand side dimension lines
ax.vlines(y - 1,
          h_lines_elevation - dy_array,
          h_lines_elevation + dy_array, colors='blue',
          linewidth=lw)

# right-hand side dimension lines
ax.vlines(x,
          h_lines_elevation - dy_array,
          h_lines_elevation + dy_array, colors='blue',
          linewidth=lw)

# dimension lines
ax.hlines(h_lines_elevation,
          y - 1, x, colors='blue', linewidth=lw)
text_elements(0.5, 0.8, '$x_1$')
text_elements(1.0, 0.7, '$x_2$')
text_elements(1.5, 0.6, '$x_3$')
text_elements(2.0, 0.5, '$x_4$')
text_elements(2.5, 0.4, '$x_5$')
text_elements(3.0, 0.3, '$x_6$')

y_elev = 1.15
x_end = 3.5
ax.vlines(0, y_elev - dy, y_elev + dy, colors='red',
          linewidth=lw)
ax.vlines(x_end, y_elev - dy, y_elev + dy, colors='red',
          linewidth=lw)
ax.hlines(y_elev, 0, 3.5, colors='red', linewidth=lw)

text_elements(x_end / 2,y_elev, r'$\bar{x}$', 'red')

ax.yaxis.set_major_locator(MultipleLocator(1.000))
plt.show()

figure_name = 'dice_moment'
fig.savefig(figure_name + '.pdf', bbox_inches='tight')
