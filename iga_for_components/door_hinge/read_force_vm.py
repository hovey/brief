#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 10:42:45 2025

@author: danajer
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.close('all')

from matplotlib import rc

def set_style_sns():
    sns.set_context('paper')
    sns.set(font = 'serif')
    sns.set(font_scale = 1.1)

    sns.set_style('white', {
        'font.family': 'serif',
        'font.serif': ['Time', 'Palatino', 'serif'],
        'lines.markersize': 10
    })


plt.rcParams.update({'font.size':8})
set_style_sns()

plt.rcParams.update({'text.usetex': False})

files = ['with_probe/results_0p8/cf_iga_data_output.json', 
         'with_probe/results_1p0/cf_iga_data_output.json',
         'with_probe/results_1p2/cf_iga_data_output.json']
mesh_sizes = ['0p8', '1p0', '1p2']
directs = ['x', 'y', 'z']

plt.figure(figsize = (10,8))

force_mag = []
vm_stresses = []
dofs = np.array([260247, 154746, 101739])
runtimes = []
for ii,file in enumerate(files):
    data = pd.read_json(file, orient = 'index')
    data_f = data['history']['pull_door_hinge']['door_hinge_reaction_force']
    time = data_f['time']
    force = np.stack([data_f['reaction_force']['x'], data_f['reaction_force']['y'], data_f['reaction_force']['z']])
    vm_stress = data['history']['pull_door_hinge']['door_hinge_max_vm']['extremum']['stress']['von_mises']
    vm_stresses.append(vm_stress[-1])
    force_mag.append(np.sqrt(force[0,-1]**2 + force[1,-1]**2 + force[2,-1]**2))
    runtimes.append(data['monitors']['pull_door_hinge']['timing']['procedure_solve'][0])
    for jj in range(3):
        plt.subplot(2,2,jj+1)
        plt.plot(time, force[jj,:], label = mesh_sizes[ii])
        
        
        if ii ==2:
            plt.xlabel('Time, s')
            plt.ylabel('door hinge reaction force, lbf')
            plt.title(directs[jj])
            plt.legend()
            plt.grid('on')
 
    plt.subplot(2,2,4)
    plt.plot(time, vm_stress, label = mesh_sizes[ii])
    if ii ==2:
        plt.xlabel('Time, s')
        plt.ylabel('door hinge von Mises, psi')
        plt.title(directs[jj])
        plt.legend()
        plt.grid('on')
       
    
force_mag = np.array(force_mag)  
vm_stresses = np.array(vm_stresses)   
runtimes = np.array(runtimes)  

plt.tight_layout()  
plt.savefig('reaction_force_comparison.png') 

plt.show()
    

plt.figure(figsize = (8,8))
plt.subplot(2,1,1)
plt.plot(dofs, force_mag, '.-', label = 'IGA')
plt.ylabel('Reaction Force Magnitude, lbf')
plt.xlabel('Number of DOFs')
plt.grid('on')
plt.legend()
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(dofs, vm_stresses, '.-', label = 'IGA')
plt.ylabel('Peak von Mises, psi')
plt.xlabel('Number of DOFs')
plt.grid('on')
plt.legend()
plt.tight_layout()
plt.savefig('door_hinge_force_vm_dofs.png')
plt.show()