# -*- coding: utf-8 -*-
"""
@author: ian spielman
"""

import os
import sys
import inspect

import numpy as np

import matplotlib.pyplot as plt
plt.style.use('../matplotlibrc') # Use this to load default settings

# this is needed to import tools from the parent directory
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import tools

#
# Overall options
# 

PDF_FileName = '../../Fig_Setup.pdf'

##############################################################################
#### Setup the full plot
##############################################################################

fig = plt.figure(1,figsize=(3.375,2.5))
height_ratios = [1,]
width_ratios = [1,]

gs = fig.add_gridspec(1, 1, 
                      height_ratios=height_ratios,
                      width_ratios=width_ratios)
gs.update(left=0.16, bottom=0.13, top=0.93, wspace=0.13, hspace=0.2, right=0.95) 

##############################################################################
#### Fake data
##############################################################################

ax = fig.add_subplot(gs[0,0])

xvals = np.linspace(0,10)
yvals = np.cos(xvals)
ax.plot(xvals, yvals, '.', color='red') 

ax.set_xlim([xvals.min(),xvals.max()])
ax.set_ylim([yvals.min(),yvals.max()])

ax.set_ylabel(r'Energy, $\hbar\omega$')
ax.set_xlabel(r'Position, $x/a$')

fig.align_ylabels()

fig.savefig(PDF_FileName, transparent=True)
