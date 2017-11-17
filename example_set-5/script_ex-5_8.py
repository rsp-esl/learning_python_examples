#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

import random
import numpy as np

# Different ways to generate random numbers

numbers = [ random.randint(-10,10) for i in range(5) ]
print (numbers)

numbers = map( lambda i: random.randint(-10,10), range(5) )
print (numbers)

numbers = np.random.randint( -10, 10, size=5 )
print (numbers)

# Apply filter() and map() to lambda constructs (anonymous functions)
numbers = range(-10,10)  # create numbers [-10, -9,. . ., 8, 9]
positives = filter( lambda x: x > 0, numbers ) # get only positive numbers
negatives = filter( lambda x: x < 0, numbers ) # get only negative numbers
print (list(positives))
print (list(negatives))

# output:
#    [-4, -3, 9, -6, -9]
#    [7, 4, 1, 7, 0]
#    [-9 -2  5  2  1]
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
##############################################################################

