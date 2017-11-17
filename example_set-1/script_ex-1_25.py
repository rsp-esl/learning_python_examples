#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

# Data structures, two-dimensional list

# 2D matrix (nested list)
m = [[1,2,3],[4,5,6],[7,8,9]]

# show the matrix (list)
for r in range( len(m) ): # for each row
    for c in range( len(m[r]) ): # for each column
        print (m[r][c],end=' ') # show the element at (r,c)
    print ('')
print ('')

# output:
#   1 2 3
#   4 5 6
#   7 8 9

##############################################################################

