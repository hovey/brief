#!/usr/bin/env python3
# lin_regress_1.py
import numpy as np
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

lw = 1 # line width for leader lines

x = np.array([1.00, 2.00, 3.00, 4.00, 5.00])
y = np.array([1.00, 2.00, 1.30, 3.75, 2.25])
theta = np.linspace(0, 2*np.pi, 100)

x_ave = np.mean(x)
y_ave = np.mean(y)

x_var = np.var(x)
y_var = np.var(y)

# the [0,1] component of the covariance matrix
xy_cov = np.cov(x, y, bias=True)[0,1]  

w_hat = xy_cov / x_var
b_hat = y_ave - w_hat * x_ave
x_lin = np.linspace(0, 6, 2)
y_lin = w_hat * x_lin + b_hat  # y = m x + b

dx = dy = 0.15
xmax = 6
ymax = 5
fig = plt.figure(figsize=(xmax, ymax))  # (width, height) inches 
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 's', color='blue', label='observation')
ax.plot(x_ave, y_ave, 'o', color='red', alpha=0.5,
 	label=r'($\bar{x},\bar{y}$) = (' + 
	'{:.2f}'.format(x_ave) + ', ' + 
	'{:.2f}'.format(y_ave) + ')')
ax.plot(x_var * np.cos(theta) + x_ave, 
	y_var * np.sin(theta) + y_ave, 
	color='green', linewidth=2.0, 
	label=r'$\sigma_x^2, \sigma_y^2$ = ' + 
	'{:.2f}'.format(x_var) + ', ' + 
	'{:.4f}'.format(y_var))
ax.plot(x_lin, y_lin, color='red', linewidth=2, 
	label=r'$y = \hat{w} x + \hat{b} = $ ' + 
	'{:.3f}'.format(w_hat) + ' $x\;+\;$' +
	'{:.3f}'.format(b_hat) )
# helper function
def text_elements(x, y, text, textcolor='green'):
	ax.text(x, y, text, backgroundcolor='white',
	ha='center', va='center', weight='normal', 
	color=textcolor)
# dimension for x_var
x_var_leader_y = 0.7
ax.plot([x_ave, x_ave + x_var], 
	x_var_leader_y * np.ones(2), color='green', 
	linewidth=1)
dy_leader = 0.1
dy_array = dy_leader * np.ones(2)
# leader lines
ax.vlines([x_ave, x_ave + x_var], 
	  x_var_leader_y - dy_array,
	  x_var_leader_y + dy_array, color='green', 
	  linewidth=1)
text_elements(x_ave + 0.5 * x_var, x_var_leader_y, 
	r'$\sigma_x^2$ = ' + 
	'{:.2f}'.format(x_var)) 
# dimension for y_var
y_var_leader_x = 0.4
ax.plot(y_var_leader_x * np.ones(2), 
	[y_ave, y_ave + y_var], 
	color='green', 
	linewidth=1)
dx_leader = dy_leader
dx_array = dx_leader * np.ones(2)
text_elements(y_var_leader_x, y_ave + 0.5 * y_var,  
	r'$\sigma_y^2$ = ' + 
	'{:.4f}'.format(y_var)) 
# leader lines

ax.hlines([y_ave, y_ave + y_var], 
	  y_var_leader_x - dx_array,
	  y_var_leader_x + dx_array,
	  color='green', 
	  linewidth=1)
ax.axis('equal')
ax.grid()
ax.set_xlabel('explanatory variable $x$')
ax.set_ylabel('response variable $y$')
ax.set_xlim(0 - dx, xmax + dx)
ax.set_ylim(0 - dy, ymax + dy)
ax.legend(loc='upper left')

plt.show()

figure_name = 'lin_regress_1'
fig.savefig(figure_name + '.pdf', bbox_inches='tight')

