#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import math, random

x = math.pow( math.pi, -1 ) # compute x = 1/PI
print ('x =', x)
print ('x =', format( x, '10.2f' ))
print ('x =', format( x, '<10.2f' ))
print ('x =', format( x, '>10.2f' ))
print ('x =', format( x, '10.2e' ))
print ('ceil(x) =', math.ceil( x ))
print ('floor(x) =', math.floor( x ))
print ('round(x) =', round( x ))

# generate a random integer between [0,16]
y = random.randint( 0, 16 ) 
print ('y =', format( y, '04b' )) # binary formatting
print ('y =', bin( y ))  # convert to binary string

s = 'hello'
print ('s = [%s]' % s.ljust(10))
print ('s = [%s]' % s.rjust(10))
print ('s = [%s]' % s.center(10))

# Output:
#    x = 0.318309886184
#    x =       0.32
#    x = 0.32      
#    x =       0.32
#    x =   3.18e-01
#    ceil(x) = 1.0
#    floor(x) = 0.0
#    round(x) = 0.0
#    y = 1010
#    y = 0b1010
#    s = [hello     ]
#    s = [     hello]
#    s = [  hello   ]

##############################################################################
