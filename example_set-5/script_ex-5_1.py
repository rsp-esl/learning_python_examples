#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

import math, numpy as np
from matplotlib import pylab

steps = 100
xs = np.linspace( 0, 1, steps+1 ) # [0.00, 0.01, ..., 0.99, 1.00]
ys = [ math.sin( 2*math.pi*x ) for x in xs ] # compute data for sin()
pylab.plot( xs, ys, label='y=sin(2*PI*x)' )  # plot data for sin()
pylab.hold( True )
ys = [ math.cos( 2*math.pi*x ) for x in xs ] # computer data for cos()
pylab.plot( xs, ys, label='y=cos(2*PI*x)' )  # plot data for cos()

pylab.title( 'Sin/Cos Plot Demo' ) # set title for the plot
pylab.xlabel( 'x', fontsize=16 ) # set label for the x-axis, font size = 16
pylab.ylabel( 'y', fontsize=16 ) # set label for the y-axis, font size = 16
pylab.legend( loc=1 ) # show legend labels at top-right corner (loc=1)
pylab.grid( True )    # turn on grid
pylab.savefig( 'output_plot-1.png', dpi=200 ) # save the figure to output file

print ('Done...')
##############################################################################
