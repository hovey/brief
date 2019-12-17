#!/usr/bin/env python
import os
import numpy as np
# import matplotlib as mpl
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from abc import ABC


rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)
# matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

# =========
class Model(ABC):
# =========
    def __init__(self):
        # origin
        self._X0, self._Y0 = 0, 0

    def origin(self):
        return [self._X0, self._Y0]

    @property
    def points(self):
        return [self._X0, self._Y0]

    @points.setter  
    def points(self, value):
        self._X0 = value[0]
        self._Y0 = value[1]


class BodyModel(Model):
    def __init__(self, width=1, height=1):
        super().__init__()
        # self._NPOINTS = 25
        self._NPOINTS = 4
        # theta = np.linspace(0.0, 2 * np.pi, self._NPOINTS)  # radians
        #self._X = np.array(radius * np.cos(theta))
        #self._Y = np.array(radius * np.sin(theta))
        self._X = width/2.0 * np.array([-1, 1, 1, -1, -1])
        self._Y = height/2.0 * np.array([-1, -1, 1, 1, -1])

    def number_of_points(self):
        return self._NPOINTS

    def perimeter(self):
        return self._X, self._Y

    @property
    def points(self):  # override
        where = 0
        X = np.insert(self._X, where, self._X0, axis=0)
        Y = np.insert(self._Y, where, self._Y0, axis=0)
        return [X, Y]

    @points.setter  # override
    def points(self, value):
        self._X0 = value[0][0]  # update the origin x
        self._Y0 = value[1][0]  # update the origin y
        self._X = value[0][1:]
        self._Y = value[1][1:]

# ========
class View(ABC):
# ========
    def __init__(self):
        self._color = 'red'

    @property
    def color(self):
        return self._color

    @color.setter  
    def color(self, value):
        self._color = value

class BodyView(View):
    def __init__(self, model, axis, color='black', ls='-'):
        super().__init__()
        self._color = color
        x, y = model.perimeter()
        # axis.plot(x, y, '-', color=self._color, linewidth=0.75)  # boundary
        axis.plot(x, y, linestyle=ls, color=self._color, linewidth=0.75)  # boundary


# ===========
# Controllers
# ===========
def offset(points, offsets=[0, 0]):
    """ Given a list of reference points [X, Y], offset them in 
    the x-axis and the y-axis.
    """
    # x = X + offset_x
    # y = Y + offset_y
    # return x, y
    x = points[0] + offsets[0]
    y = points[1] + offsets[1]
    return [x, y]

def simple_shear(points, shear_12=0):
    """ Given a list of reference points [X, Y], simple shear them in 
    the x-axis by distance shear_x (Length) to the current points [x, y].
    """
    # x = X + shear_12 * Y
    # y = Y
    # return x, y
    x = points[0] + shear_12 * points[1]
    y = points[1]
    return [x, y]

def rotate(points, angle=0):
    """ Given list of reference points [X, Y], rotate them about the 
    z-axis by angle R (radians) to the current points [x, y].
    """
    # x = np.cos(R) * X - np.sin(R) * Y
    # y = np.sin(R) * X + np.cos(R) * Y
    X = points[0]
    Y = points[1]
    x = np.cos(angle) * X - np.sin(angle) * Y
    y = np.sin(angle) * X + np.cos(angle) * Y
    return [x, y]

def stretch(points, stretches=[1, 1]):
    """ Given a list of reference points [X, Y], simple stretch j
    by factor stretches[0] in the x-direction and 
    by factor stretches[1] in the y-direction 
    to the current points [x, y].
    """
    x = stretches[0] * points[0]
    y = stretches[1] * points[1]
    return [x, y]


# ======
# client
# ======
fig = plt.figure(figsize=(6, 6))  # inches, (wide, tall)
ax = fig.add_subplot(1, 1, 1)

RADTODEG = 180.0/np.pi
DEGTORAD = 1.0/RADTODEG

def text(x, y, text, txt_align='center', txt_color='black'):
    ax.text(x, y, text, backgroundcolor="white",
        ha=txt_align, va='center_baseline', weight='bold', color=txt_color)

# horizontal and vertical dividing lines
edge = 8
#ax.plot([-edge, edge], [0, 0], '--', linewidth=1, color='dimgray')
#ax.plot([0, 0], [-edge, edge], '--', linewidth=1, color='dimgray')

#b1 = BodyModel(width=4, height=2)  # create, subfigure (a)
#c = 4  # notational origin (center) for each of the four plots
#m = c + 3  # motional origin plus margin
#inner = 1.5  # inner margin position
#o = [-c, -c/2]  # offset
#b1.points = offset(b1.points, o)  # read then update
#gb = BodyView(b1, ax, 'black')  # view

# https://tex.stackexchange.com/questions/7669/bfseries-is-to-textbf-as-what-is-to-textsf/7670

ax.axis('equal')

# major axes
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
#ax.grid(b=True, which='major', linestyle=':')
ax.grid(b=True, which='major', linestyle='solid', linewidth=0.5, color='lightgray')

# minor axes
# no operations

ax.set_xlabel(r'Jacobian $J$')
#ax.set_ylabel(r'$X_2, x_2$')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
# ax.legend(loc='lower right', framealpha=1.0)

ax.set_xticklabels(['', '', '', '', '', -1, '', '', '', 0, '', '', '', 1, '', '', ''])
#ax.set_yticklabels(['', '', -3, -2, -1, 0, 1, 2, 3, '', -3, -2, -1, 0, 1, 2, 3])
#ax.set_yticklabels(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])

#text(-edge + 1, edge - 1, '(a)')
#text(edge - 1, edge - 1, '(b)')
#text(-edge + 1, -edge + 1, '(c)')
#text(edge - 1, -edge + 1, '(d)')

xtxt, ytxt = 0, 7
dy = 1
# w, h = 16, 10
b = BodyModel(width=16, height=10)  
#b.points = offset(b.points, [xtxt, ytxt - 0.6])  # read then update
b.points = offset(b.points, [0, 2.5])  # read then update
BodyView(b, ax, 'dimgray')  # view
text(xtxt, ytxt, 'general motion', txt_color='dimgray')

xtxt = -2.5
ytxt = ytxt - 1.5 * dy
# w, h = 5, 1.25
b = BodyModel(width=11, height=9)  # overwrite
b.points = offset(b.points, [-2.5, 2])  # read then update
BodyView(b, ax)  # view
text(xtxt, ytxt, 'homogeneous motion')

xtxt = -4
ytxt = 4
w, h = 5, 1.25
b = BodyModel(width=w, height=h)  # overwrite
b.points = offset(b.points, [xtxt, ytxt])  # read then update
BodyView(b, ax, ls='--')  # view
text(xtxt, ytxt, 'rigid body motion')

xtxt = 3
w = 6
b = BodyModel(width=w, height=h)  # overwrite
b.points = offset(b.points, [xtxt, ytxt])  # read then update
BodyView(b, ax)  # view
text(xtxt, ytxt, 'deformable body motion')

xtxt = -6
ytxt = ytxt - 2 * dy
w = 3.25
b = BodyModel(width=w, height=h)  # overwrite
b.points = offset(b.points, [xtxt, ytxt])  # read then update
BodyView(b, ax, ls='--')  # view
text(xtxt, ytxt, 'translation $\\bar{\\boldsymbol{u}}$')

xtxt = -2
b = BodyModel(width=w, height=h)  # overwrite
b.points = offset(b.points, [xtxt, ytxt])  # read then update
BodyView(b, ax, ls='--')  # view
text(xtxt, ytxt, 'rotation \\sffamily\\bfseries R')

xtxt = 3
b = BodyModel(width=w, height=h)  # overwrite
b.points = offset(b.points, [xtxt, ytxt])  # read then update
BodyView(b, ax)  # view
text(xtxt, ytxt, 'stretch \\sffamily\\bfseries U v')

#xtxt = -3.5
ytxt = ytxt - 3 * dy
y5 = -1  # row 5 from top
#w = 2
b = BodyModel(width=2, height=h)  # overwrite
x_shear = -3.5
b.points = offset(b.points, [x_shear, y5])  # read then update
BodyView(b, ax, ls='--')  # view
text(x_shear, ytxt, 'shear')

#xtxt = 0.5
#w = 4
b = BodyModel(width=4, height=h)  # overwrite
x_dil = 0.5
b.points = offset(b.points, [x_dil, y5])  # read then update
BodyView(b, ax)  # view
text(x_dil, ytxt, 'dilitation $\\Delta V / V$')

# arrows underyling the 'contraction' and 'expansion' labels
xtxt = 2  # overwrite
ytxt = -5  # overwrite
#ax.plot(-8, ytxt, 'o', color='red')  
ax.plot(-4, ytxt, 'o', color='red')  
ax.plot(0, ytxt, 'o', color='red')  
ax.plot(4, ytxt, 'o', color='red')  
b = BodyModel(width=5.5, height=h)  # overwrite
b.points = offset(b.points, [2.3, -3.5])  # read then update
BodyView(b, ax, ls='--')  # view
#ax.plot(8, ytxt, 'o', color='red')  
ap = dict(arrowstyle='->') # arrow properites, overwrite
ax.annotate('isochoric motion $J=1$', xy=(4, ytxt), xytext=(0, ytxt + 1.25), arrowprops=ap)
ap = dict(arrowstyle='<->') # arrow properites, overwrite
ax.annotate('', xy=(-8, ytxt), xytext=(-4, ytxt), arrowprops=ap)
ax.annotate('', xy=(-4, ytxt), xytext=(0, ytxt), arrowprops=ap)
ax.annotate('', xy=(0, ytxt), xytext=(4, ytxt), arrowprops=ap)
ax.annotate('', xy=(4, ytxt), xytext=(8, ytxt), arrowprops=ap)
text(-3 * xtxt, ytxt, 'expansion')
text(-xtxt, ytxt, 'contraction')
text(xtxt, ytxt, 'contraction')
text(3 * xtxt, ytxt, 'expansion')

ytxt = -6 # overwrite
ax.plot(0, ytxt, 'o', color='green')  
ap = dict(arrowstyle='<-') # arrow properites, overwrite
# ap = dict(arrowstyle='->') # arrow properites, overwrite
ax.annotate('', xy=(0, ytxt), xytext=(-8, ytxt), arrowprops=ap)
ax.annotate('', xy=(0, ytxt), xytext=(8, ytxt), arrowprops=ap)
text(-2 * xtxt, ytxt, 'inversion')
text(2 * xtxt, ytxt, 'non-version')

ap = dict(arrowstyle='->') # arrow properites, overwrite
ax.annotate('singular', xy=(0, ytxt), xytext=(0.5, ytxt - 1), arrowprops=ap)

# ax.text(b1.origin()[0] - 0.55, b1.origin()[1] - 0.55, '$\\boldsymbol{x}$') # no white background
# ax.text(b4.origin()[0] - 0.5, b4.origin()[1] - 0.5, '$\\boldsymbol{x}$')


# fig.tight_layout()
plt.show()

print_to_pdf = 0
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

