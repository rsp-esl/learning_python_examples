#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

def _sqr( x ): # define a function to compute x^2
    return (x**2)

squares = [ x*x for x in range(10) ] # compute 0^2, 1^2, . . ., 9^2
print (squares)

# Python supports the creation of anonymous functions at runtime,
# using a construct called 'lambda'.
sqr = lambda x: x*x
squares = [ _sqr(x) for x in range(10) ]
print (list(squares))

# map anonymous function to a list
squares = map( sqr, range(10) )
print (list(squares))

# map the function ‘_sqr’ to a list
squares = map( _sqr, range(10 ) )
print (list(squares))

# Output:
#    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

##############################################################################

