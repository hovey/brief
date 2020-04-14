import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

LATEX = 1
SERIALIZE = 1
VERBOSE = 0

if LATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)

n_intervals = 5  # max number of intervals reqd is 4 to illustrate cubic b-spline
fs = 2**8  # sample frequency (number of samples per interval)
print(f'Using sample frequency of {fs}')
nts = fs * n_intervals # number of time steps
t = np.linspace(0, n_intervals, nts+1)
if VERBOSE:
    print(f't={t}')

def N0(i, t, fs):
    N = 0.0 * t
    N[i*fs:(i+1)*fs] = 1.0
    if VERBOSE:
        print(f'N0 with i={i} is')
        print(N)
    return N

def N1(i, t, fs):
    N = 0.0 * t
    # N[i*fs:(i+1)*fs] = np.linspace(0, fs, fs)/fs
    N[i*fs:(i+1)*fs] = t[0:fs]  # first interval
    # N[(i+1)*fs:(i+2)*fs] = (i+1) - np.linspace(0, fs, fs)/fs
    N[(i+1)*fs:(i+2)*fs] = 2.0 - t[fs:2*fs]  # second interval
    if VERBOSE:
        print(f'N1 with i={i} is')
        print(N)
    return N

def N2(i, t, fs):
    N = 0.0 * t
    t1 = t[0:fs]  # first time interval
    N[i*fs:(i+1)*fs] = 0.5 * t1 * t1  # first interval
    t2 = t[fs:2*fs]  # second time interval
    t3 = t[2*fs:3*fs]  # third time interval
    # t2 = t1
    # N[(i+1)*fs:(i+2)*fs] = 2.0 - t2  # second interval
    # N[(i+1)*fs:(i+2)*fs] = 0.5 * (-2 * t2 * t2 + 2 * t2 + 1)  # second interval
    # N[(i+1)*fs:(i+2)*fs] = 0.5 * (-2 * t2 * t2 + 6 * t2 + 3)  # second interval
    # N[(i+1)*fs:(i+2)*fs] = 0.5 * (-2 * t2 * t2 + 6 * t2 - 1)  # second interval
    # N[(i+1)*fs:(i+2)*fs] = 0.5 * (-2 * t2 * t2 + 6 * t2 - 3)  # second interval
    N[(i+1)*fs:(i+2)*fs] = 0.5*(t2*(2-t2) + (3-t2)*(t2-1))  # second interval
    N[(i+2)*fs:(i+3)*fs] = 0.5 * (3 - t3)**2  # third interval
    if VERBOSE:
        print(f't1 is {t1}')
        print(f't2 is {t2}')
        print(f't3 is {t3}')
        print(f'N2 with i={i} is')
        print(N)
    return N


fig = plt.figure(figsize=(6, 6))  # x in inches wide, y inches tall
# fig = plt.figure(figsize=(8, 8))  # x in inches wide, y inches tall
# s = 8  # inches, characteristic dimension for figure
# fig = plt.figure(figsize=(s/4, s))  # x in inches wide, y inches tall
# fig = plt.figure()  # x in inches wide, y inches tall
ax0 = fig.add_subplot(3, 1, 1, aspect=1)
ax1 = fig.add_subplot(3, 1, 2, aspect=1, sharex=ax0, sharey=ax0)
ax2 = fig.add_subplot(3, 1, 3, aspect=1, sharex=ax0, sharey=ax0)

# globals
kwargs = {
    'alpha' : 0.8,
    'linewidth' : 2
}
linestyles = ['dashed', 'solid', 'dashdot', 'solid', 'dotted']
ap = dict(arrowstyle='->')  # arrow properties

# constant (p=0)
# ax0.plot(t, N0(0, t, fs), **kwargs)
# ax0.plot(t, N0(1, t, fs), **kwargs)
# ax0.plot(t, N0(2, t, fs), **kwargs)
# ax0.plot(t, N0(3, t, fs), **kwargs)
p = 0
for i in range(n_intervals - p):
    ax0.plot(t, N0(i, t, fs), linestyle=linestyles[i], **kwargs)

ax0.set_ylabel(r'constant')
ax0.grid()

# linear (p=1)
p = 1
# ax1.plot(t, N1(0, t, fs), **kwargs)
# ax1.plot(t, N1(1, t, fs), **kwargs)
# ax1.plot(t, N1(2, t, fs), **kwargs)
for i in range(n_intervals - p):
    ax1.plot(t, N1(i, t, fs), linestyle=linestyles[i], **kwargs)

ax1.set_ylabel(r'linear')
ax1.grid()

# quadratic (p=2)
p = 2
# ax2.plot(t, N2(0, t, fs), **kwargs)
# ax2.plot(t, N2(1, t, fs), **kwargs)
for i in range(n_intervals - p):
    ax2.plot(t, N2(i, t, fs), linestyle=linestyles[i], **kwargs)

ax2.set_ylabel(r'quadratic')
ax2.grid()

dt = 0.5  # applies to all x-axes b/c previously shared
ax0.xaxis.set_major_locator(MultipleLocator(dt))
ax0.yaxis.set_major_locator(MultipleLocator(dt))
ax0.set_ylim([-0.05, 1.4])


# ax0.annotate(r'$N_{i,0}(t)$', xy=(0.5, 0.5), xytext=(b0_x, b0_y), arrowprops=ap, ha='center', va='bottom')
ty = 1.1  # text y coordinate
ax0.text(0.5, ty, r'$N_{i,0}(t)$', ha='center', va='baseline')
ax0.text(1.5, ty, r'$N_{i+1,0}(t)$', ha='center', va='baseline')
ax0.text(2.5, ty, r'$N_{i+2,0}(t)$', ha='center', va='baseline')
ax0.text(3.5, ty, r'$N_{i+3,0}(t)$', ha='center', va='baseline')
ax0.text(4.5, ty, r'$N_{i+4,0}(t)$', ha='center', va='baseline')

ax1.text(1.0, ty, r'$N_{i,1}(t)$', ha='center', va='baseline')
ax1.text(2.0, ty, r'$N_{i+1,1}(t)$', ha='center', va='baseline')
ax1.text(3.0, ty, r'$N_{i+2,1}(t)$', ha='center', va='baseline')
ax1.text(4.0, ty, r'$N_{i+3,1}(t)$', ha='center', va='baseline')

ax2.text(1.5, ty, r'$N_{i,2}(t)$', ha='center', va='baseline')
ax2.text(2.5, ty, r'$N_{i+1,2}(t)$', ha='center', va='baseline')
ax2.text(3.5, ty, r'$N_{i+2,2}(t)$', ha='center', va='baseline')

plt.xticks([0, 1, 2, 3, 4, 5], [r'$i$', r'$i+1$', r'$i+2$', r'$i+3$', r'$i+4$', r'$i+5$'])
# plt.xticks(np.arange(n_intervals+1).tolist(), [r'$i$', r'$i+1$', r'$i+2$', r'$i+3$', r'$i+4$'])

plt.show()

if SERIALIZE:
  fig.savefig("bspline.pdf", bbox_inches="tight")
