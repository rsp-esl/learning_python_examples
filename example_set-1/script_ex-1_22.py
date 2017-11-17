#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## String manipulation

s = 'a,b,c,d,e,f'  # define a string
print (s.replace( ',', ':')) # replace all ',' with ':'

# output:
#   a:b:c:d:e:f

s = s.replace( ',', '' )   # remove  all ',' 
print (s)        # output: abcdef
print (s[:])     # same as s[0:]
print (s[:-1])   # get all characters, except the last char
print (s[-1])    # get the first char from right 
print (s[-2:-1]) # get the second char from right
print (s[1:-1])  # get all chars, except the first & last char

# output:
#   abcdef
#   abcdef
#   abcde
#   f
#   e
#   bcde
##############################################################################
