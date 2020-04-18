#!/usr/bin/env python3
# bernstein_extended.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

import bernstein_polynomial as bp

LATEX = 1
SERIALIZE = 0

if LATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)

nts = 101 # number of time steps, include t0 as a step
nti = nts - 1 # number of time intervals
t = np.linspace(0, 1, nts)  # parameterization

# fig = plt.figure(figsize=(6, 6))  # x in inches wide, y inches tall
fig = plt.figure(figsize=(6.5, 6.5))  # x in incmes wide, y inches tall
ax2 = fig.add_subplot(2, 2, 3, aspect=1)
ax0 = fig.add_subplot(2, 2, 1, aspect=1)
ax3 = fig.add_subplot(2, 2, 4, aspect=1, sharey=ax2)
ax1 = fig.add_subplot(2, 2, 2, aspect=1, sharey=ax0, sharex=ax3)

# globals
ap = dict(arrowstyle='->')  # arrow properties
lax, lay = 0.5, 1.1
b0_x = 0.32
b0_y = 0.87
dx = 0.008
annotate_dict = dict(arrowprops=ap, 
    ha='center', 
    va='bottom',
    backgroundcolor='white')
text_dict = dict(ha='center', 
    va='bottom',
    backgroundcolor='white')
linestyle_tuple = ('solid', 'dashed', 'dashdot')

p = 5
for q in np.arange(p+1):
    ls = linestyle_tuple[q % len(linestyle_tuple)]
    ax0.plot(t, bp.bernstein_polynomial(q, p, nti), linestyle=ls)

ax0.annotate(r'$b_{0,5}(t)$', xy=(0.06-dx, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax0.text(lax, b0_y, r'$\ldots$', **text_dict)
ax0.annotate(r'$b_{5,5}(t)$', xy=(0.94+dx, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax0.xaxis.set_major_locator(MultipleLocator(0.25))
ax0.yaxis.set_major_locator(MultipleLocator(0.25))
ax0.set_ylabel(r'$b_{i,p}(t)$')
ax0.text(lax, lay, r'(a) $p=5$', **text_dict)
ax0.grid()
plt.setp(ax0.get_xticklabels(), visible=False)

p = 6
for q in np.arange(p+1):
    ls = linestyle_tuple[q % len(linestyle_tuple)]
    ax1.plot(t, bp.bernstein_polynomial(q, p, nti), linestyle=ls)

ax1.annotate(r'$b_{0,6}(t)$', xy=(0.06-2*dx, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax1.text(lax, b0_y, r'$\ldots$', **text_dict)
ax1.annotate(r'$b_{6,6}(t)$', xy=(0.94+2*dx, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)
ax1.xaxis.set_major_locator(MultipleLocator(0.25))
ax1.yaxis.set_major_locator(MultipleLocator(0.25))
ax1.text(lax, lay, r'(b) $p=6$', **text_dict)
ax1.grid()
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=False)

p = 7
for q in np.arange(p+1):
    ls = linestyle_tuple[q % len(linestyle_tuple)]
    ax2.plot(t, bp.bernstein_polynomial(q, p, nti), linestyle=ls)

ax2.annotate(r'$b_{0,7}(t)$', xy=(0.06-3*dx, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax2.text(lax, b0_y, r'$\ldots$', **text_dict)
ax2.annotate(r'$b_{7,7}(t)$', xy=(0.94+3*dx, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax2.xaxis.set_major_locator(MultipleLocator(0.25))
ax2.yaxis.set_major_locator(MultipleLocator(0.25))
ax2.set_xlabel(r'$t$')
ax2.set_ylabel(r'$b_{i,p}(t)$')
ax2.text(lax, lay, r'(c) $p=7$', **text_dict)
ax2.grid()

p = 8
for q in np.arange(p+1):
    ls = linestyle_tuple[q % len(linestyle_tuple)]
    ax3.plot(t, bp.bernstein_polynomial(q, p, nti), linestyle=ls)

ax3.annotate(r'$b_{0,8}(t)$', xy=(0.06-4*dx, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax3.text(lax, b0_y, r'$\ldots$', **text_dict)
ax3.annotate(r'$b_{8,8}(t)$', xy=(0.94+4*dx, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax3.xaxis.set_major_locator(MultipleLocator(0.25))
ax3.yaxis.set_major_locator(MultipleLocator(0.25))
ax3.set_xlabel(r'$t$')
ax3.text(lax, lay, r'(d) $p=8$', **text_dict)
ax3.grid()
plt.setp(ax3.get_yticklabels(), visible=False)

plt.show()

if SERIALIZE:
  fig.savefig("bernstein_extended.pdf", bbox_inches="tight")
