#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Python package 're' (regular expression)

import re # import regular expression module
# make a pattern matcher for numbers (int or float)
pattern = re.compile( '[-+]?[0-9]*\.?[0-9]+' ) 

s = '123.45:abc:-120:-0.25'
for t in s.split( ':' ):
    m = pattern.match( t )
    if ( m != None ):
        print ('Match found: ', m.group())

# output:
#  Match found: 123.45
#  Match found: -120
#  Match found: -0.25

print( ' '.join( pattern.findall( s ) ) )

# output: 123.45 -120 -0.25

##############################################################################
