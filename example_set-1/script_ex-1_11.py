#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Datastructures, Lists

# make a list of four elements (strings).
list1 = ['One', 'Two', 'Three', 'Four']
for s in list1:            # for each element in the list
    print (s,end=' ')      # print the element, without newline
print ("")

# output: One Two Three Four

list2 = range(1,5) # create a list containing 1,..,4
for i in list2:    # for each element in the list
    print (i,end=' ')      # print the element
print ( "")

# output: 1 2 3 4

list3 = list1[:]   # make a copy of the entire list
for i in range( len(list3) ):
    print (list3[i],end=' ')
print ("")

# output: One Two Three Four

##############################################################################
