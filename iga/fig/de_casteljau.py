import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

LATEX = 1
SERIALIZE = 0
SERIALIZE_SEQUENCE = 1

if LATEX:
  rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
  rc('text', usetex=True)

nts = 101 # number of time steps, include t0 as a step
t = np.linspace(0, 1, nts) # parameterization
tm = 0.5 # midpoint

# three control points in 2D
P00 = np.array([[0], [6]])
P10 = np.array([[6], [2]])
P20 = np.array([[10], [8]])
x = 0 # index
y = 1 # index

# linear Bezier 
P01 = P00 * (1 - t) + P10 * t
P11 = P10 * (1 - t) + P20 * t

# quadratic Bezier
P02 = P01 * (1 - t) + P11 * t

# plt.figure(0)
fig = plt.figure(figsize=(8, 4))  # x in inches wide, y inches tall
ax = fig.add_subplot(1, 2, 1, aspect=1)
ax2 = fig.add_subplot(1, 2, 2, aspect=1)

dx, dy = 0.35, 0.35
ax.plot(P01[x], P01[y], linestyle='dotted', color='red')
ax.plot(P01[x,0], P01[y,0], marker='o', color='red')
ax.text(P01[x,0], P01[y,0] - dy, r'$P_0$', ha='right', va='top')
# now again on ax2
ax2.plot(P01[x], P01[y], linestyle='dotted', color='red')
ax2.plot(P01[x,0], P01[y,0], marker='o', color='red')
ax2.text(P01[x,0], P01[y,0] - dy, r'$P_{0,0}$', ha='right', va='top')

ax.plot(P11[x], P11[y], linestyle='dotted', color='red')
ax.plot(P11[x,0], P11[y,0], marker='o', color='red')
ax.text(P11[x,0], P11[y,0] - 2*dy, r'$P_1$', ha='center', va='top')
ax.plot(P11[x,-1], P11[y,-1], marker='o', color='red')
ax.text(P11[x,-1] + dx, P11[y,-1] - dy, r'$P_2$', ha='left', va='top')
ax.plot(P02[x], P02[y], color='black')
# now again on ax2
ax2.plot(P11[x], P11[y], linestyle='dotted', color='red')
ax2.plot(P11[x,0], P11[y,0], marker='o', color='red')
ax2.text(P11[x,0], P11[y,0] - 2*dy, r'$P_{1,0}$', ha='center', va='top')
ax2.plot(P11[x,-1], P11[y,-1], marker='o', color='red')
ax2.text(P11[x,-1] + dx, P11[y,-1] - dy, r'$P_{2,0}$', ha='left', va='top')
ax2.plot(P02[x], P02[y], color='black')

# linear Bezier at t=0.5
tm = 0.5  # overwrite previous parameterization, not plot just single point
P01m = P00 * (1 - tm) + P10 * tm
P11m = P10 * (1 - tm) + P20 * tm

ax.plot([P01m[x], P11m[x]], [P01m[y], P11m[y]], linestyle='dashed', color='green')
ax2.plot([P01m[x], P11m[x]], [P01m[y], P11m[y]], linestyle='dashed', color='green')

ax.plot(P01m[x], P01m[y], marker='o', color='green')
ax.text(P01m[x] - dx, P01m[y] - dy, r'$Q_0(t=0.5)$', ha='right', va='top')
ax2.plot(P01m[x], P01m[y], marker='o', color='green')
ax2.text(P01m[x] - dx, P01m[y] - dy, r'$P_{0,1}(t=0.5)$', ha='right', va='top')

ax.plot(P11m[x], P11m[y], marker='o', color='green')
ax.text(P11m[x] + dx, P11m[y] - dy, r'$Q_1(t=0.5)$', ha='left', va='top')
ax2.plot(P11m[x], P11m[y], marker='o', color='green')
ax2.text(P11m[x] + 0.6*dx, P11m[y] - dy, r'$P_{1,1}(t=0.5)$', ha='left', va='top')

# quadratic Bezier at t=0.5
P02m = P01m * (1 - tm) + P11m * tm
ax.plot(P02m[x], P02m[y], marker='o', color='black')
ax.text(P02m[x], P02m[y] + dy, r'$Q(t=0.5)$', ha='center', va='bottom')
ax2.plot(P02m[x], P02m[y], marker='o', color='black')
ax2.text(P02m[x] - dx, P02m[y] + dy, r'$P_{0,2}(t=0.5)$', ha='center', va='bottom')

ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.yaxis.set_major_locator(MultipleLocator(2.0))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax2.xaxis.set_major_locator(MultipleLocator(2.0))
ax2.yaxis.set_major_locator(MultipleLocator(2.0))
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')

lax, lay = -1, 9
ax.text(lax, lay, '(a)', backgroundcolor='white', ha='center', va='baseline')
ax2.text(lax, lay, '(b)', backgroundcolor='white', ha='center', va='baseline')
ax.grid()
ax2.grid()
ax.set_xlim(-2, 12)
ax.set_ylim(0, 10)
ax2.set_xlim(-2, 12)
ax2.set_ylim(0, 10)
# ax.legend()

plt.show()

if SERIALIZE:
  fig.savefig("de_casteljau.pdf", bbox_inches="tight")


# plt.figure()
nrow, ncol = 2, 3
# fig2 = plt.figure(figsize=(3*ncol, 3*nrow))  # x in inches wide, y inches tall
# fig2 = plt.figure(figsize=(10.5, 5))  # x in inches wide, y inches tall, hard code to match 10 x 14 grid on figure
fig2 = plt.figure(figsize=(6.5, 3.25))  # x in inches wide, y inches tall, hard code 
tcapture = np.linspace(0, 1, 6)  # 0, 0.2, 0.3, ..., 1.0
for i in range(nrow):
  for j in range(ncol):
    s = i*ncol + j + 1
    # print(f'Processing sequence item s={s}')
    # ax = fig2.add_subplot(nrow, ncol, i*ncol + j + 1, aspect=1)
    ax = fig2.add_subplot(nrow, ncol, s, aspect=1)
    # k = int( (i*ncol + j + 1)/(nrow*ncol) * nts ) - 1
    k = (np.abs(t - tcapture[s-1])).argmin()  # find the index closest to the tcapture times
    # print(f'Processing index k={k}')
    # 
    ax.plot(P01[x,0:k+1], P01[y,0:k+1], linestyle='dotted', color='red')
    ax.plot(P01[x,0], P01[y,0], marker='o', color='red')
    #
    ax.plot(P11[x,0:k+1], P11[y,0:k+1], linestyle='dotted', color='red')
    ax.plot(P11[x,0], P11[y,0], marker='o', color='red')
    #
    ax.plot([P01[x,k], P11[x,k]], [P01[y,k], P11[y,k]], linestyle='dashed', color='green')
    ax.plot(P01[x,k], P01[y,k], marker='o', color='green')
    ax.plot(P11[x,k], P11[y,k], marker='o', color='green')
    #
    ax.plot(P02[x,0:k+1], P02[y,0:k+1], color='black')
    ax.plot(P02[x,k], P02[y,k], marker='o', color='black')
    #
    ax.set_xlim(-2, 12)
    ax.set_ylim(0, 10)
    ax.xaxis.set_major_locator(MultipleLocator(2.0))
    ax.yaxis.set_major_locator(MultipleLocator(2.0))
    ax.grid()
    # turn off tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # ax.set_xlabel(r'$x$')
    # ax.set_ylabel(r'$y$')
    ti = '{:.1f}'.format(t[k])
    ax.text(lax, lay - dy, 't='+ti, backgroundcolor='white', ha='left', va='baseline')

plt.tight_layout()  # prevent subfigure overlap https://matplotlib.org/3.2.1/tutorials/intermediate/tight_layout_guide.html
plt.show()

if SERIALIZE_SEQUENCE:
  filename = 'de_casteljau_sequence.pdf'
  fig2.savefig(filename, bbox_inches="tight")
  print(f'Save {filename}.')
