#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Function range()

print (range(1,10)) # print a list of integers 1,2,..,9

# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = range(10)  # create a list of integers 1,2,...,9
print ('a =', a, ', length =', len(a))
print ('First element in the list : ', a[0])
print ('Last element in the list  : ', a[len(a)-1])

# output: a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , length = 10
# output: First element in the list :  0
# output: Last element in the list  :  9

for i in range(-5,5,2):
    print (i,end=' ')
print ('')

# output: -5 -3 -1 1 3

##############################################################################
