#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

# In Python, strings are immutable.
# note x,y,z,t point to the same string object.

x = 'Hello World!'
print ('id(x)=%i, x=[%s]' % (id(x), x))

y = """Hello World!"""
print ('id(y)=%i, y=[%s]' % (id(y), y))

z = y + ''
print ('id(z)=%i, z=[%s]' % (id(z), z))

t = x[:]
print ('id(t)=%i, t=[%s]' % (id(t), t))

u = x[0:-1] + x[-1]
print ('id(u)=%i, u=[%s]' % (id(u), u))

# Output:
#    id(x)=140613506706320, x=[Hello World!]
#    id(y)=140613506706320, y=[Hello World!]
#    id(z)=140613506706320, z=[Hello World!]
#    id(t)=140613506706320, t=[Hello World!]
#    id(u)=140613506707048, u=[Hello World!]

##############################################################################
