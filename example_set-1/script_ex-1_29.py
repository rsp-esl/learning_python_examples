#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Set manipulation

# check whether s1 is a subset of s2
def issubset( s1, s2 ):
    if len(s1) == 0:
        return True
    for e in s1:
        if e not in s2:
            return False
    return True

s1 = set([]); s2 = set([1,2,3]); s3 = set([2,3])

print (issubset(s1, s2), issubset(s2, s1))
print (issubset(s2, s3), issubset(s3, s2))
print (len(s1 - s2), len(s2 - s1))
print (len(s2 - s3), len(s3 - s2))

# output:
#  True False
#  False True
#  0 3
#  1 0
##############################################################################
