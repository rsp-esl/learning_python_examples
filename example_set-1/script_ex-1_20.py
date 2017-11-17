#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## String manipulation

s = 'nobody@localhost'
# find a substring 
print (s.find( '@', 0 ))       # output: 6

index = s.find( '!', 0 )       # find a substring
if ( index == -1 ):
    print ('not found')
else:
    print ('found at index = ', index)

print (s.startswith( 'nobody' ))  # output: True
print (s.endswith( 'localhost' )) # output: True

s = 'We love Python!'
print (s.upper())                 # output: WE LOVE PYTHON!
print (s.lower())                 # output: we love python!
print (s.capitalize())            # output: We love python!

##############################################################################
