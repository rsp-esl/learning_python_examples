#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Function definition, function argument list, default values

# define a functions with arguments that have default values
def func( a, b=1, c=0 ):
    return a*b + c

# function calls
print (func(1))
print (func(a=1))
print (func(-1,5))
print (func(-1,1,1))
print (func( a=-1, c=3))

# output:
#  1
#  1
#  -5
#  0
#  2

##############################################################################
