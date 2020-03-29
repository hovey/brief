import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

USELATEX = 1
SAVEFIG = 1

if USELATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)



x = np.linspace(0, 1, 100)
y = np.sin(np.pi * x)

x0 = np.linspace(0, 0.5, 50)
s0 = 2*x0

x1 = np.linspace(0.5, 1, 50)
s1 = 1 - 2*(x1 - 0.5)

fig = plt.figure(figsize=(8, 8))  # in inches wide, 8 inches tall
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.plot(x, y, color='navy', label=r'$f(x) = \sin(\pi x)$')
# ax.plot(x0, s0, color='red', label=r'$S_0(x) = 2 x$')
# ax.plot(x1, s1, color='green', label=r'$S_1(x) = 2 - 2 x$')
ax.plot(x0, s0, marker='o', linestyle='dashed', markevery=[0], label=r'$S_0(x) = 2 x$')
ax.plot(x1, s1, marker='o', linestyle='dashdot', markevery=[0], label=r'$S_1(x) = 2 - 2 x$')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.grid()

ax.legend()

plt.show()

if SAVEFIG:
  fig.savefig("linear_spline.pdf", bbox_inches="tight")

