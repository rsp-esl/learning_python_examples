#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists

numbers = [0,-1,2,-2,1,-3,3] # create a list of int
numbers = sorted( numbers )  # sort the list
print (numbers) # show the numbers in the (sorted) list

# output: [-3, -2, -1, 0, 1, 2, 3]

# create a list of positive numbers from a list
positives = [ n for n in numbers if (n > 0) ]
print (positives)

# output: [1, 2, 3]

# create a list of negative numbers from a list
negatives = [ n for n in numbers if (n < 0) ]
print (negatives)

# output: [-3, -2, -1]

squares = [ i*i for i in numbers ]
print (squares)
print (sum(squares))

# output: [9, 4, 1, 0, 1, 4, 9]
# output: 28

##############################################################################

