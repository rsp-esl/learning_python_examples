#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## math calculation, math package

# import math module for sqrt(), pow(), exp(),
#   log10(), sin(), cos(), atan(), etc.
# see: http://docs.python.org/library/math.html

import math

# compute 10 to the power of 3
print ("10^3 = %d" % (10**3))         # 10^3 = 1000

# compute 2 to the power of 10
print ("2^10 = %d" % int(pow(2,10)))  # 2^10 = 1024

# compute 'e'
print ("e = %.7f" % math.exp(1))        # e = 2.71828182846

# compute the Golden ratio: 
                                      # Golden ratio = 1.61803398875
print ("Golden ratio = %f" % ((1 + math.sqrt(5))/2) )  

##############################################################################

