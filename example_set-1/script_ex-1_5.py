#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## math calculation, math package

import math

# In Python, two types of numbers are 'int' and 'float'.
x = 1      # assign 1 to variable x
y = 1.0    # assign 1.0 to variable y

print ("x = {:d}, y = {:.3f}".format(x,y) ) # show the values of x and y
print ("type(x) = " + str(type(x)))  # show type of x, type(x) = <type 'int'>
print ("type(y) = " + str(type(y)))  # show type of y,  type(y) = <type 'float'>

# compute Polar coordinates of (x,y)
print ("r = " + str(math.sqrt( x*x + y*y )))           # r = 1.41421356237
print ("theta = " + str(math.atan( y/x )) + " rad.")   # theta = 0.785398163397 rad.

deg = 180 * math.atan( y/x ) / math.pi 
print ("theta = {:.2f} deg.".format(deg))              # theta = 45.0 deg.

##############################################################################
