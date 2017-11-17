#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

from math import sin, cos, pi

angles = [0, pi/4, pi/2, 3*pi/4, pi, 2*pi]
u = [sin(x)**2 + cos(x)**2 for x in angles]
print ('u =', u)

from math import factorial

for n in range(1,5):
    print ('%d! = %d' % (n, factorial(n))) # compute factorial n!

# Output:
#    u = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#    1! = 1
#    2! = 2
#    3! = 6
#    4! = 24

##############################################################################

