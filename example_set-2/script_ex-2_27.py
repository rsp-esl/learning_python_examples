#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

x = [ 0,1,2,3 ]
y = [ 'a', 'b', 'c', 'd' ]

z = zip(x,y) # produces a list of two-tuples by using zip()
print ('z =', list(z))

t = [ (b,a) for a,b in zip(x,y) ]
print ('t =', list(t))

t = map( lambda z: (z[1],z[0]), zip(x,y) )
print ('t =', list(t))

a = [0,1,2,3]
b = [1,0,-1,1]
print ('a =', a)
print ('b =', b)

c = map( lambda x,y: x*y, a, b )
print ('c =', list(c))

g = (lambda x, y: x*y )
d = map( g, a, b )
print ('d =', list(d))

# Output:
# z = [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
# t = [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
# t = [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
# a = [0, 1, 2, 3]
# b = [1, 0, -1, 1]
# c = [0, 0, -2, 3]
# d = [0, 0, -2, 3]

##############################################################################

