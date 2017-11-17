#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

import math, numpy as np
from matplotlib import pyplot as plt

plt.figure( figsize=(6,6) )

labels = [ 'A', 'B', 'C', 'D', 'E' ]
counts = [ 35, 20, 13, 30, 2 ]
total = sum(counts)
percents = [ ('%.1f' % (100.0*x/total))+'%' for x in counts]

plt.pie( counts, labels=labels )
plt.title( 'Pie Chart', fontsize=18 ) 
plt.legend( tuple(percents), loc=1, fontsize=10 ) 
plt.savefig( 'output_plot-7.png', dpi=200 )

print ('Done...')
##############################################################################

