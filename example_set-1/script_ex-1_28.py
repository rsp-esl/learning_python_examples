#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

# Data structures, Sets, Set manipulation

s1 = set( [1,2,2] )     # define a set named s1
s2 = set( [1,2,3,4,5])  # define a set named s2
print ('s1 =', s1, ', s2 =', s2)
print ('union(s1,s2) =', (s1 | s2))
print ('intersection(s1,s2) =', (s1 & s2))
print ('difference(s1,s2) =', (s1 - s2))
print ('difference(s2,s1) =', (s2 - s1))

# output: 
#   s1 = set([1, 2]) , s2 = set([1, 2, 3, 4, 5])
#   union(s1,s2) = set([1, 2, 3, 4, 5])
#   intersection(s1,s2) = set([1, 2])
#   difference(s1,s2) = set([])
#   difference(s2,s1) = set([3, 4, 5])

for e in (s1 | s2) - (s1 & s2):
    print (e,end=' ')
print ('')

# output: 3 4 5

##############################################################################
