#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

import math, numpy as np
from matplotlib import pyplot

xs = np.arange( 0, 10, 0.05 ) # generate x data between [0,10), 0.05 step
ys = [ [ 1.0 - math.exp(-x) for x in xs ], [ math.exp(-x) for x in xs ] ]
ylabels = [ 'y=1-exp(-x)', 'y=exp(-x)' ] 
styles  = [ 'r.', 'b.' ] # red-dot and blue-dot styles
pyplot.figure() # create a figure
for i in range(2):
    pyplot.subplot( 2, 1, i+1 ) # use subplot (i+1) on a 2x1 grid 
    pyplot.xlim( 0, 10 )  # set xmin, xmax for x-axis
    pyplot.ylim( 0, 1.1 ) # set ymin, ymax for y-axis
    pyplot.xlabel( 'x' )  # set label for x-axis
    pyplot.ylabel( ylabels[i] ) # set label for y-axis
    pyplot.subplots_adjust( hspace=0.5 ) # set horizontal spacing
    pyplot.title( 'Subplot %i' % (i+1), fontsize=16 ) # add title, font size=16 
    pyplot.plot( xs, ys[i], styles[i] ) 

pyplot.savefig( 'output_plot-6.png', dpi=200 ) # save the figure to a PNG file

print ('Done...')
##############################################################################

