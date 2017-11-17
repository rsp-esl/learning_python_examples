#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## function format(), and format specifiers

value = 12345.6789

# format_specifier: one digit after decimal point
print (format( value, '.1f' ))

# output: 12345.7

# format_specifier: with comma, one digit after decimal point 
print (format( value, ',.1f' ))

# output: 12,345.7

# format_specifier: scientific notation
print (format( value, '.3e' ))

# output: 1.235e+04

# format_specifier: 8 positions
print ('[' + format( value, '8.1f') + ']')

# output: [ 12345.7]

# format_specifier: 8 positions, with comma
print ('[' + format( int(value), '8,d') + ']')

# output: [  12,345]

##############################################################################

