#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

import math, numpy as np
from matplotlib import pyplot as plt

xs = np.arange( -1.0, 1.05, 0.05 ) # generate x data: [-1.00,-0.95,..,0.95,1.00] 
plt.figure() # create a figure
plt.xlabel( 'x' )  # set x-label
plt.ylabel( 'y' )  # set y-label
plt.title( 'Plot XY' ) # set title
plt.axis( [-1,1, 0,1] ) # set limits for x-axis and y-axis
plt.grid( True ) # show grid
plt.hold( True ) # keep all plots

ys = [ 1-x*x for x in xs ] # generate y data for the first plot
plt.plot( xs, ys, 'b-', label='y=1-x^2' ) # xy-plot
ys = [ x*x for x in xs ] # generate y data for the second plot
plt.plot( xs, ys, 'g-', label='y=x^2' ) # xy-plot 
plt.legend( loc='upper right' ) # show legend at upper-right corner
plt.savefig( 'output_plot-3.png', dpi=200 ) # save the figure as a PNG file

print ('Done...')
##############################################################################
