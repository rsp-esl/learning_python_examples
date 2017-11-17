#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

# This is a function generator.
def g( n ):
    for i in range(n):
        yield i

# This is a generator object.
o = g(5)
for x in o:
   print (x)

print ('-'*20)

o = g(5)
try:
    while True:
       print (next(o))  # or o.next()
except StopIteration:
    pass
print ('-'*20)

print (sum( g(5) ))     # output: 10
print (list( g(5) ))    # output: [0, 1, 2, 3, 4]

print ('-'*20)

g = ( x*x for x in range(5) ) # this is a generator expression
print (sum(g))

g = ( (x,y) for x in range(1,3) for y in range(1,3) )
print (list(g))  # output: [(1, 1), (1, 2), (2, 1), (2, 2)]

# Output:
#    0
#    1
#    2
#    3
#    4
#    --------------------
#    0
#    1
#    2
#    3
#    4
#    --------------------
#    10
#    [0, 1, 2, 3, 4]
#    --------------------
#    30
#    [(1, 1), (1, 2), (2, 1), (2, 2)]

##############################################################################
