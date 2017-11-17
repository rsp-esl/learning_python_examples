#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, List manipulation

n = 5
numbers = [ 2*i + 1 for i in range(n) ] # create a list
print (numbers[:])    # a new list with all elements
print (numbers[0:])   # a new list with all elements
print (numbers[:-1])  # ... with all except the last element
print (numbers[:-2])  # ... all except the last two elements
print (numbers[-1:])  # ... only the last element
print (numbers[-2:])  # ... the last two elements
print (numbers[1:-1]) # ... all except the first and last

# output:
#  [1, 3, 5, 7, 9]
#  [1, 3, 5, 7, 9]
#  [1, 3, 5, 7]
#  [1, 3, 5]
#  [9]
#  [7, 9]
#  [3, 5, 7]

##############################################################################
