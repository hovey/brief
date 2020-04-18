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
# ap = dict(arrowstyle='->')  # arrow properties
# lax, lay = 0.5, 1.11
# b0_x = 0.32
# b0_y = 0.87

p = 5
for q in np.arange(p+1):
    ax0.plot(t, bp.bernstein_polynomial(q, p, nti))

p = 6
for q in np.arange(p+1):
    ax1.plot(t, bp.bernstein_polynomial(q, p, nti))

p = 7
for q in np.arange(p+1):
    ax2.plot(t, bp.bernstein_polynomial(q, p, nti))

p = 8
for q in np.arange(p+1):
    ax3.plot(t, bp.bernstein_polynomial(q, p, nti))

plt.show()

if SERIALIZE:
  fig.savefig("bernstein_extended.pdf", bbox_inches="tight")
