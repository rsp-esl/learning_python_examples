#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## String manipulation

# join strings in the list using ',' as separator
print (','.join( ['aaa','bbb','ccc'] ))

# output: aaa,bbb,ccc

numbers = [1,2,3,  4,  5]
print (str(numbers)) # [1, 2, 3, 4, 5]
print (','.join(map(str,numbers))) # 1,2,3,4,5

lines = """\
Line One
Line Two
Line Three
"""

# split lines and removing line breaks (CR,LF,CRLF)
for line in lines.splitlines(False):
    print ('"' + line + '"')

# output:
#  "Line One"
#  "Line Two"
#  "Line Three"

##############################################################################
