#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## String manipulation

s = 'aaa:bbb:ccc:ddd'  # define a string
substrings = []        # create an empty list

# split a string into substrings, use ';' as separator
substrings = s.split(':') # create a list of strings

print ("number of substrings = ", len(substrings))

for k in range ( len(substrings) ):
    print (substrings[k],end=' ')  # access the element by index
print ('')

for s in substrings: # for each element, print it 
    print (s,end=' ')
print ('')

# output:
#  number of substrings = 4
#  aaa bbb ccc ddd
#  aaa bbb ccc ddd

##############################################################################

