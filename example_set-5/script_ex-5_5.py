#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Python package 'NumPy', 'mathplotlib'

from matplotlib.pylab import *

def f1(t):
    return t**2*exp(-t**2)
    
def f2(t):
    return t**2*f1(t)

t = linspace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)
plot(t, y1, 'r-' )
hold( 'on' )
plot(t, y2, 'bo' )
xlabel( 't' )
ylabel( 'y' )
legend( [r'$t^2*\,e^{(-t^2)}$', r'$t^4*\,e^{(-t^2)}$'] )
title( 'Plotting two curves in the same plot' )
show()

##############################################################################

