#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Function definition, function argument list

# Variable number of arguments
def fx( a, b, *others):
    print (a, b,end=' ')
    for x in others:
        print (x,end=' ')
    print ('')

fx(0,1)
fx(0,1,2)
fx(0,1,2,3,4)

# output:
#  0 1 
#  0 1 2 
#  0 1 2 3 4

##############################################################################
