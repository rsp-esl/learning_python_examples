#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import cmath # complex-number mathematics

x = cmath.sqrt(-1)
print ('x = sqrt(-1) =', x)
print ('1/x =', 1/x)
print ('1j*x =', 1j*x)
print ('1j*1j =', 1j*1j)

y = 1 - 1j
print ('y =', y)

y = complex(1,-1) # create a complex number object
print ('y =', y)
print ('Re(y)=', y.real) # the real part of y
print ('Im(y)=', y.imag) # the imaginary part of y

z = y.conjugate() # compute the conjugate of y
print ('z =', z)
print ('y*z =', y*z)
print ('|z| =', abs(z))

# Output:
#    x = sqrt(-1) = 1j
#    1/x = -1j
#    1j*x = (-1+0j)
#    1j*1j = (-1+0j)
#    y = (1-1j)
#    y = (1-1j)
#    Re(y)= 1.0
#    Im(y)= -1.0
#    z = (1+1j)
#    y*z = (2+0j)
#    |z| = 1.4142135623730951

##############################################################################

