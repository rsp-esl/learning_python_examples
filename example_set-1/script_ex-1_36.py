#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Python package 're' (regular expression)

import re # import regular expression module

s = '01101aaaBBB'

# replace any 0 or 1 with * 
print (re.sub( '[01]', '*', s ))

# output: *****aaaBBB

# replace any substring containing only 0 or 1 with - 
print (re.sub( '[01]+', '-', s ))

# output: -aaaBBB

# replace any letter with .
print (re.sub( '[a-zA-Z]', '.', s ))

# output: 01101......

# replace any non-letter with .
print (re.sub( '[^a-zA-Z]', '.', s ))

# output: .....aaaBBB

##############################################################################

