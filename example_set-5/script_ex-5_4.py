#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

import math, numpy as np
from matplotlib import pyplot as plt

ns = np.arange( 1, 16.5, 1.0 ) # generate data for n: 1..16 

# create a figure (figure size in inches)
plt.figure( figsize=(6.0,5.0), dpi=100 ) # use resolution 100 dot-per-inch

plt.xlabel( 'n' )      # set x-label
plt.ylabel( 'f(n)' )   # set y-label
plt.title( 'Plot XY' ) # set title
plt.axis( [1, 16, 0, 80] ) # set limits for x-axis and y-axis
plt.grid( True ) # show grid
plt.title( 'Growth functions', fontsize=14 ) # add title to the figure
plt.hold( True ) # keep all plots

fs = [ n for n in ns ] 
plt.plot( ns, fs, 'y-o', label=r'$n$' ) # yellow line + o marker
fs = [ n*n for n in ns ] 
plt.plot( ns, fs, 'y-x', label=r'$n^2$' ) # yellow line + x marker
fs = [ math.pow(2,n) for n in ns ]
plt.plot( ns, fs, 'b-', label=r'$2^n$' ) # blue line 
fs = [ math.log(n) for n in ns ] 
plt.plot( ns, fs, 'g-x', label=r'$log_2(n)$' ) # green line + x marker
fs = [ n*math.log(n) for n in ns ] 
plt.plot( ns, fs, 'g-', label=r'$n\ log_2(n)$' ) # green line

plt.legend( loc='upper right' ) # show legend at upper-right corner
plt.savefig( 'output_plot-4.png', dpi=200 ) # save the figure as a PNG file

print ('Done...')

# Lines: - solid line, --  dashed line, -. dash-dot line, : dotted line
# Colors: b blue, g green, r red, c cyan, m magenta, y  yellow, k black, w white
# Symbols: . points,  o circle symbols, ^ triangle up symbols, v triangle down symbols, 
#          s square symbols, + plus symbols, x cross symbols, D diamond symbols,
#          d thin diamond symbols, ...


##############################################################################

