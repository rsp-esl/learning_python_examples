#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, List manipulation

numbers = [1,2,3,4,5] # create a list of integers
del numbers[-1]       # delete the last element
del numbers[0]        # delete the first element
print (numbers)       # show all remaining elements 

# output: [2, 3, 4]

numbers.append(-1)    # add -1 at the end of the list
numbers.insert(0,5)   # insert 5 to the list at index 0
print (numbers)

# output: [5, 2, 3, 4, -1]

numbers.sort()        # sort the list
print (numbers)

# output: [-1, 2, 3, 4, 5]

del numbers[0:]       # delete all elements
print (numbers)

# output: []

##############################################################################
