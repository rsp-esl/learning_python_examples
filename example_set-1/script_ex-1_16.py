#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Sets

s1 = set(['a','b','b','c']) # create a set from a list
s2 = set(['b','c','d','e','d'])

print ('s1 =', s1, len(s1))
print ('s2 =', s2, len(s2))
print ('f' in s1)   # check for membership
print (s1 & s2)   # print intersection
print (s1 | s2)   # print union
print (s1 - s2)   # print difference 
print (s2 - s1)   # print difference 
print (s1 ^ s2) 
print ((s1 | s2) - (s1 & s2))

# Output:
#   s1 = set(['a', 'c', 'b']) 3
#   s2 = set(['c', 'b', 'e', 'd']) 4
#   False
#   set(['c', 'b'])
#   set(['a', 'c', 'b', 'e', 'd'])
#   set(['a'])
#   set(['e', 'd'])
#   set(['a', 'e', 'd'])
#   set(['a', 'e', 'd'])
##############################################################################
