import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

LATEX = 1
SERIALIZE = 0

if LATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)

nts = 101 # number of time steps, include t0 as a step
t = np.linspace(0, 1, nts)  # parameterization

b01 = (1 - t)
b11  = t

b02 = (1 - t)**2
b12 = 2 * t * (1 - t)
b22 = t**2

b03 = (1 - t)**3 
b13 = 3 * t * (1 - t)**2
b23 = 3 * t**2 * (1 - t)
b33 = t**3

b04 = (1 - t)**4
b14 = 4 * t * (1 - t)**3
b24 = 6 * t**2 * (1 - t)**2
b34 = 4 * t**3 * (1 - t)
b44 = t**4

# fig = plt.figure(figsize=(6, 6))  # x in inches wide, y inches tall
fig = plt.figure(figsize=(6.5, 6.5))  # x in incmes wide, y inches tall
ax2 = fig.add_subplot(2, 2, 3, aspect=1)
ax0 = fig.add_subplot(2, 2, 1, aspect=1)
ax3 = fig.add_subplot(2, 2, 4, aspect=1, sharey=ax2)
ax = fig.add_subplot(2, 2, 2, aspect=1, sharey=ax0, sharex=ax3)

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

# linear
ax0.plot(t, b01, linestyle='solid')
ax0.plot(t, b11, linestyle='dashed')

ax0.annotate(r'$b_{0,1}(t)$', xy=(0.25, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax0.annotate(r'$b_{1,1}(t)$', xy=(0.75, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax0.xaxis.set_major_locator(MultipleLocator(0.25))
ax0.yaxis.set_major_locator(MultipleLocator(0.25))
# ax0.set_xlabel(r'$t$')
plt.setp(ax0.get_xticklabels(), visible=False)
# ax0.set_ylabel(r'linear $b_{i,1}(t)$')
ax0.set_ylabel(r'$b_{i,p}(t)$')
ax0.text(lax, lay, r'(a) linear ($p=1$)', **text_dict)
ax0.grid()

# quadratic
ax.plot(t, b02, linestyle='solid')
ax.plot(t, b12, linestyle='dashed')
ax.plot(t, b22, linestyle='dashdot')

ax.annotate(r'$b_{0,2}(t)$', xy=(0.125, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax.annotate(r'$b_{1,2}(t)$', xy=(0.5, 0.5), xytext=(0.5, 0.63), **annotate_dict)
ax.annotate(r'$b_{2,2}(t)$', xy=(0.875, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
# ax.set_xlabel(r'$t$')
plt.setp(ax.get_xticklabels(), visible=False)
# ax.set_ylabel(r'quadratic $b_{i,2}(t)$')
plt.setp(ax.get_yticklabels(), visible=False)
ax.text(lax, lay, r'(b) quadratic ($p=2$)', **text_dict)
ax.grid()
# ax.legend()

# cubic
ax2.plot(t, b03, linestyle='solid')
ax2.plot(t, b13, linestyle='dashed')
ax2.plot(t, b23, linestyle='dashdot')
ax2.plot(t, b33, linestyle='solid')

ax2.annotate(r'$b_{0,3}(t)$', xy=(0.085, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax2.annotate(r'$b_{1,3}(t)$', xy=(0.333, 0.44), xytext=(0.333, 0.63), **annotate_dict)
ax2.annotate(r'$b_{2,3}(t)$', xy=(0.667, 0.44), xytext=(0.667, 0.63), **annotate_dict)
ax2.annotate(r'$b_{3,3}(t)$', xy=(0.915, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax2.xaxis.set_major_locator(MultipleLocator(0.25))
ax2.yaxis.set_major_locator(MultipleLocator(0.25))
ax2.set_xlabel(r'$t$')
# ax2.set_ylabel(r'cubic $b_{i,3}(t)$')
ax2.set_ylabel(r'$b_{i,p}(t)$')
ax2.text(lax, lay, r'(c) cubic ($p=3$)', **text_dict)
ax2.grid()

# quartic
ax3.plot(t, b04, linestyle='solid')
ax3.plot(t, b14, linestyle='dashed')
ax3.plot(t, b24, linestyle='dashdot')
ax3.plot(t, b34, linestyle='solid')
ax3.plot(t, b44, linestyle='dashed')

ax3.annotate(r'$b_{0,4}(t)$', xy=(0.06, 0.75), xytext=(b0_x, b0_y), **annotate_dict)
ax3.annotate(r'$b_{1,4}(t)$', xy=(0.25, 0.42), xytext=(0.25, 0.63), **annotate_dict)
ax3.annotate(r'$b_{2,4}(t)$', xy=(0.5, 0.375), xytext=(0.5, 0.63), **annotate_dict)
ax3.annotate(r'$b_{3,4}(t)$', xy=(0.75, 0.42), xytext=(0.75, 0.63), **annotate_dict)
ax3.annotate(r'$b_{4,4}(t)$', xy=(0.94, 0.75), xytext=(1-b0_x, b0_y), **annotate_dict)

ax3.xaxis.set_major_locator(MultipleLocator(0.25))
ax3.yaxis.set_major_locator(MultipleLocator(0.25))
ax3.set_xlabel(r'$t$')
# ax3.set_ylabel(r'quartic $b_{i,4}(t)$')
plt.setp(ax3.get_yticklabels(), visible=False)
ax3.text(lax, lay, r'(d) quartic ($p=4$)', **text_dict)
ax3.grid()

plt.show()

if SERIALIZE:
  fig.savefig("bernstein.pdf", bbox_inches="tight")
