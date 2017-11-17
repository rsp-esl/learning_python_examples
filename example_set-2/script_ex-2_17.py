#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

x = 123.4567
s = 'x = %.3E' % x  # scientific notation
print (s)

for i in range(10):
   print ('%02d' % i,end=' ') # show integer number with leading zeros
print ('')

# format string
x, y, z = 2, -3, 9
s = '({0},{1},{2})'.format( x,y,z )
print (s)

s = '{a} {b}'.format( a='Hello', b='World!' )
print (s)

x = 12.36732
y = -202.4
s = '{m:.4f}, {n:.3e}'.format( m=x, n=y )
print (s)

# Output:
#   x = 1.235E+02
#   00 01 02 03 04 05 06 07 08 09 
#   (2,-3,9)
#   Hello World!
#   12.3673, -2.024e+02

##############################################################################
