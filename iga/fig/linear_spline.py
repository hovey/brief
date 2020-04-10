import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

USELATEX = 1
SAVEFIG = 1

if USELATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)

# three-point interpolation

x = np.linspace(0, 1, 100)
y = np.sin(np.pi * x)

x0 = np.linspace(0, 0.5, 50)
s0 = 2*x0

x1 = np.linspace(0.5, 1, 50)
s1 = 1 - 2*(x1 - 0.5)

fig = plt.figure(figsize=(4, 8))  # x in inches wide, y inches tall
ax = fig.add_subplot(2, 1, 1, aspect=1)
ax2 = fig.add_subplot(2, 1, 2, aspect=1)

ax.plot(x, y, color='navy', label=r'$f(x) = \sin(\pi x)$')
ax.plot(x0, s0, marker='o', linestyle='dashed', markevery=[0], label=r'$S_0(x) = 2 x$')
ax.plot(x1, s1, marker='o', linestyle='dashdot', markevery=[0], label=r'$S_1(x) = 1 - 2(x-1/2)$')

ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
lax, lay = 0.1, 0.9
ax.text(lax, lay, '(a)', backgroundcolor='white', ha='center', va='baseline')
ax.grid()
ax.legend()

# five-point interpolation

x0 = np.linspace(0, 0.25, 25)
s0 = 2 * np.sqrt(2) * x0

x1 = np.linspace(0.25, 0.50, 25)
s1 = np.sqrt(2)/2 + (4 - 2*np.sqrt(2)) * (x1 - 1/4)

x2 = np.linspace(0.50, 0.75, 25)
s2 = 1 + (2*np.sqrt(2) - 4) * (x2 - 2/4)

x3 = np.linspace(0.75, 1, 25)
s3 = np.sqrt(2)/2 - 2*np.sqrt(2) * (x3 - 3/4) 

ax2.plot(x, y, color='navy', label=r'$f(x) = \sin(\pi x)$')
ax2.plot(x0, s0, marker='o', linestyle='dashed', markevery=[0], label=r'$S_0(x)$')
ax2.plot(x1, s1, marker='o', linestyle='dashdot', markevery=[0], label=r'$S_1(x)$')
ax2.plot(x2, s2, marker='o', linestyle='dotted', markevery=[0], label=r'$S_2(x)$')
ax2.plot(x3, s3, marker='o', linestyle='solid', markevery=[0], label=r'$S_3(x)$')

ax2.xaxis.set_major_locator(MultipleLocator(0.25))
ax2.yaxis.set_major_locator(MultipleLocator(0.25))
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.text(lax, lay, '(b)', backgroundcolor='white', ha='center', va='baseline')
ax2.grid()
ax2.legend()

plt.show()

if SAVEFIG:
  fig.savefig("linear_spline.pdf", bbox_inches="tight")

