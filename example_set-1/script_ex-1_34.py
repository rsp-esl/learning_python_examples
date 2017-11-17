#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, Tuples

num_list = [3,4,5]             # create a list of integers 
num_tuple = (0,1,2)            # creaet a tuple of integers 
num_tuple += tuple( num_list ) # convert to tuple and append to a tuple
print (num_tuple)              # output: (0,1,2,3,4,5)

str = "10, 20, 30, 40"
tup = tuple( int(i) for i in str.split(',') ) # convert str to tuple
print (tup)                    # output: (10, 20, 30, 40)

tup = (10,20,30,40)
total = sum( x for x in tup )  # sum all elements of a tuple of integers
print ('total = ', total)      # output: total= 100 

tup = ('a','b','c','d')        # create a tuple of strings
s = ','.join( x for x in tup)  # join all elements of a tuple into a string
print (s)                      # output: a,b,c,d

##############################################################################
