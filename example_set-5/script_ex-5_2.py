#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

import math, numpy as np
from matplotlib import pyplot # providing a MATLAB-like plotting framework

xs = np.arange( 0, 10, 0.05 ) # generate x data between [0,10), 0.05 step
ys = [ 1.0 - math.exp(-x) for x in xs ] # generate y data 
pyplot.figure() # create a figure 
pyplot.xlim( 0, 10 )  # set xmin, xmax for x-axis
pyplot.ylim( 0, 1.1 ) # set ymin, ymax for y-axis
pyplot.xlabel( 'x' )  # set label for x-axis
pyplot.ylabel( 'y=1-exp(-x)' ) # set label for y-axis
pyplot.title( 'Plot XY', fontsize=14 ) # add title text, font size = 14 
pyplot.plot( xs, ys, 'r-' ) # use red line

pyplot.savefig( 'output_plot-2.png', dpi=200 ) # export as a PNG file
pyplot.savefig( 'output_plot-2.svg' ) # export the figure as an SVG file
pyplot.savefig( 'output_plot-2.pdf' ) # export the figure as a PDF file

print ('Done...')
##############################################################################
