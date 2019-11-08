"""
Demo of axis spines
from matplotlib.org/examples/ticks_and_spines/spines_demo.html

Reference:
http://matplotlib.org/examples/pylab_examples/subplots_demo.html
http://matplotlib.org/users/usetex.html
http://matplotlib.org/users/customizing.html
http://matthiaseisen.com/pp/patterns/p0203/
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as patches

initial_offset_x1 = 2
initial_offset_x2 = 2
x1 = np.array([1,2,3,1,2,3,1,2,3]) - initial_offset_x1
x2 = np.array([1,1,1,2,2,2,3,3,3]) - initial_offset_x2

plt.close('all')

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('grid', linestyle='dotted', color='gray')

size = 5

plt.axes().add_patch(
  patches.Rectangle(
    (x1[0], x2[0]), # (x,y) corner point
    x1[-1]-x1[0],   # width
    x2[-1]-x2[0],   # height
    facecolor="blue",
    alpha = 0.1
  )
)
plt.plot(x1, x2, 'bo')
plt.axis([-size, size, -size, size])
plt.grid(True)
plt.axes().set_aspect('equal')
plt.axes().set_xticks(np.arange(-size, size+1, 1))
plt.axes().set_yticks(np.arange(-size, size+1, 1))
plt.xlabel(r'position ($X_1$)')
plt.ylabel(r'position ($X_2$)')
plt.title(r'reference configuration ($t=t_0$)')

#plt.show()
plt.savefig('configuration_reference.pdf', orientation='landscape', format='pdf')
#fig.savefig('test.pdf')
#plt.close(fig)

u1 = 3
u2 = 2

x1t = x1 + u1
x2t = x2 + u2

plt.axes().add_patch(
  patches.Rectangle(
    (x1t[0], x2t[0]), # (x,y) corner point
    x1t[-1]-x1t[0],   # width
    x2t[-1]-x2t[0],   # height
    facecolor="red",
    alpha = 0.1
  )
)
plt.plot(x1t, x2t, 'ro')
plt.title(r'current configuration ($t>t_0$)')
plt.savefig('configuration_current.pdf', orientation='landscape', format='pdf')

plt.close('all')

# volumetric motion

stretch = 2
x1t = stretch*x1
x2t = stretch*x2

plt.axes().add_patch(
  patches.Rectangle(
    (x1[0], x2[0]), # (x,y) corner point
    x1[-1]-x1[0],   # width
    x2[-1]-x2[0],   # height
    facecolor="blue",
    alpha = 0.1
  )
)
plt.plot(x1, x2, 'bo')
plt.axis([-size, size, -size, size])
plt.grid(True)
plt.axes().set_aspect('equal')
plt.axes().set_xticks(np.arange(-size, size+1, 1))
plt.axes().set_yticks(np.arange(-size, size+1, 1))
plt.xlabel(r'position ($X_1$)')
plt.ylabel(r'position ($X_2$)')
plt.title(r'reference configuration ($t=t_0$)')

plt.axes().add_patch(
  patches.Rectangle(
    (x1t[0], x2t[0]), # (x,y) corner point
    x1t[-1]-x1t[0],   # width
    x2t[-1]-x2t[0],   # height
    facecolor="red",
    alpha = 0.1
  )
)
plt.plot(x1t, x2t, 'ro')
plt.title(r'current configuration ($t>t_0$)')
#plt.show()
plt.savefig('configuration_volumetric.pdf', orientation='landscape', format='pdf')


plt.close('all')

# biaxial motion

stretch_1 = 2
stretch_2 = 0.5
x1t = stretch_1*x1
x2t = stretch_2*x2

plt.axes().add_patch(
  patches.Rectangle(
    (x1[0], x2[0]), # (x,y) corner point
    x1[-1]-x1[0],   # width
    x2[-1]-x2[0],   # height
    facecolor="blue",
    alpha = 0.1
  )
)
plt.plot(x1, x2, 'bo')
plt.axis([-size, size, -size, size])
plt.grid(True)
plt.axes().set_aspect('equal')
plt.axes().set_xticks(np.arange(-size, size+1, 1))
plt.axes().set_yticks(np.arange(-size, size+1, 1))
plt.xlabel(r'position ($X_1$)')
plt.ylabel(r'position ($X_2$)')
plt.title(r'reference configuration ($t=t_0$)')

plt.axes().add_patch(
  patches.Rectangle(
    (x1t[0], x2t[0]), # (x,y) corner point
    x1t[-1]-x1t[0],   # width
    x2t[-1]-x2t[0],   # height
    facecolor="red",
    alpha = 0.1
  )
)
plt.plot(x1t, x2t, 'ro')
plt.title(r'current configuration ($t>t_0$)')
plt.savefig('configuration_stretch.pdf', orientation='landscape', format='pdf')


