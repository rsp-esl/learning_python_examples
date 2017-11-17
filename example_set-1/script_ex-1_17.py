#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Function definition

# define a function in Python
# compute factorial, n must be non-negative integer
def fac(n):
    if ( n == 0 ):
        return 1
    else:
        return n * int(fac( n-1 ))

for i in range(10):
    print (fac(i),end=' ')  # call the function

# output: 1 1 2 6 24 120 720 5040 40320 362880

##############################################################################

