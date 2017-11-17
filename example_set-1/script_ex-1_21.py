#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## String manipulation, function len()

s = '\t\tHello World! \r\n'
print (len(s)) # compute the length of string, output: 17

# remove white-space characters in the string
print (len( s.lstrip() )) # left-side strip,   output: 15
print (len( s.rstrip() )) # right-side strip,  output: 14
print (len( s.strip() ))  # both-side strip,   output: 12 

s = s.strip()
print ("'%s'" % s)        # output: 'Hello World!'

##############################################################################

