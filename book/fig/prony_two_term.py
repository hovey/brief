#!/usr/bin/env python

import os
import numpy as np
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

lw = 2 # line width 

G_infinity = 1.0 # Pa, long-term shear modulus
G_max = 7.0
G_0 = G_max * G_infinity # Pa, initial shear

y_ax_min = 0.0
y_ax_max = 8.0

tau_old = 1.4286e-3 # seconds
tau_new = 2.5e-2 # seconds

t_final = 0.100 # seconds
delta_t = 0.0005 # seconds
t = np.arange(0, t_final, delta_t)   # seconds, plot limits to be [ 0, t_final ]
G_t_old = G_infinity + (G_0 - G_infinity) * np.exp(-t / tau_old)
G_t_new = G_infinity + (G_0 - G_infinity) * np.exp(-t / tau_new)

fig = plt.figure(figsize=(6, 4))  # x inches wide, y inches tall

ax = fig.add_subplot(1, 1, 1)
ax.plot(t, G_t_old, 
        color='magenta', 
        linestyle='--', 
        linewidth=lw+1, 
        label=r'$\tau =$ (1/700) s = 1.43e$^{-3}$ s', 
        zorder=4)

t_mid = -tau_new * np.log(0.5)
G_mid = (G_0 + G_infinity)/2.0

ax.vlines([t_mid], [y_ax_min], [G_mid], zorder=4)
ax.hlines([G_mid], [0.0], [t_mid], zorder=4)
nudge_t = 0.0005 # s
nudge_y = 0.25 # G units
ax.text(t_mid + nudge_t, G_mid + nudge_y, 
        r'$(t_{\mbox{\footnotesize mid}}, G_{\mbox{\footnotesize mid}})$ = (1.73e$^{-2}$ s, 4.0)',
        backgroundcolor='white')

ax.plot(t, G_t_new, 
        color='blue', 
        linewidth=lw+1, 
        label=r'$\tau = \;\;$(1/40) s~~=~2.50e$^{-2}$ s', 
        zorder=4)
#ax.plot(t, np.exp(-t/0.05), 
#        color='green', 
#        linewidth=lw+1, 
#        label=r'$\tau =$ 5.00e$^{-2}$ s')
ax.grid()
ax.set_xlabel('time $t$ (seconds)')
ax.set_ylabel(r'shear stress $G(t) = G_{\infty} + (G_0 - G_{\infty}) \exp(-t/ \tau)$')
ax.set_xlim( 0, t_final)
ax.set_ylim(y_ax_min, y_ax_max)
ax.legend(loc='upper right')

# helper functions
def text_elements(x, y, text, textcolor='blue'):
    ax.text(x, y, text, backgroundcolor='white',
            ha='center', va='center', weight='normal', color=textcolor)

text_elements(0.010, G_0 - 0.05,  r'$G_0$ = ' + str(G_max), textcolor='black')
text_elements(0.090, 0.60, r'$G_{\infty}$ = ' + str(G_infinity), textcolor='black')

plt.show()

print_to_pdf = 1
if print_to_pdf:
    script_name = os.path.basename(__file__)
    figure_name = os.path.splitext(script_name)[0]
    print(f'Saving figure as {figure_name}.pdf')
    fig.savefig(figure_name + '.pdf', bbox_inches='tight')

