import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

LATEX = 1
SERIALIZE = 1

if LATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)

nts = 101 # number of time steps, include t0 as a step
t = np.linspace(0, 1, nts)  # parameterization

b02 = (1 - t)**2
b12 = 2 * t * (1 - t)
b22 = t**2

b03 = (1 - t)**3 
b13 = 3 * t * (1 - t)**2
b23 = 3 * t**2 * (1 - t)
b33 = t**3

fig = plt.figure(figsize=(4, 8))  # x in inches wide, y inches tall
ax = fig.add_subplot(2, 1, 1, aspect=1)
ax2 = fig.add_subplot(2, 1, 2, aspect=1)

# quadratic
ax.plot(t, b02, linestyle='solid')
ax.plot(t, b12, linestyle='dashed')
ax.plot(t, b22, linestyle='dashdot')

ap = dict(arrowstyle='->')  # arrow properties
ax.annotate(r'$b_{0,2}(t)$', xy=(0.125, 0.75), xytext=(0.375, 0.875), arrowprops=ap, 
  ha='center', va='bottom')
ax.annotate(r'$b_{1,2}(t)$', xy=(0.5, 0.5), xytext=(0.5, 0.65), arrowprops=ap, 
  ha='center', va='bottom')
ax.annotate(r'$b_{2,2}(t)$', xy=(0.875, 0.75), xytext=(0.625, 0.875), arrowprops=ap, 
  ha='center', va='bottom')

ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$b_{i,2}(t)$')
lax, lay = 0.15, 0.90
ax.text(lax, lay, '(a)', backgroundcolor='white', ha='center', va='baseline')
ax.grid()
# ax.legend()

# cubic
ax2.plot(t, b03, linestyle='solid')
ax2.plot(t, b13, linestyle='dashed')
ax2.plot(t, b23, linestyle='dashdot')
ax2.plot(t, b33, linestyle='solid')

ax2.annotate(r'$b_{0,3}(t)$', xy=(0.085, 0.75), xytext=(0.375, 0.875), arrowprops=ap, 
  ha='center', va='bottom')
ax2.annotate(r'$b_{1,3}(t)$', xy=(0.333, 0.44), xytext=(0.375, 0.65), arrowprops=ap, 
  ha='center', va='bottom')
ax2.annotate(r'$b_{2,3}(t)$', xy=(0.667, 0.44), xytext=(0.625, 0.65), arrowprops=ap, 
  ha='center', va='bottom')
ax2.annotate(r'$b_{3,3}(t)$', xy=(0.915, 0.75), xytext=(0.625, 0.875), arrowprops=ap, 
  ha='center', va='bottom')

ax2.xaxis.set_major_locator(MultipleLocator(0.25))
ax2.yaxis.set_major_locator(MultipleLocator(0.25))
ax2.set_xlabel(r'$t$')
ax2.set_ylabel(r'$b_{i,3}(t)$')
ax2.text(lax, lay, '(b)', backgroundcolor='white', ha='center', va='baseline')
ax2.grid()

plt.show()

if SERIALIZE:
  fig.savefig("bernstein.pdf", bbox_inches="tight")
