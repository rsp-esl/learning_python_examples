#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

word = 'Yes!'
# access each character in the string
for ch in word:
    print ("'%c'" % (ch),end=' ')
print ('')

# output: 'Y' 'e' 's' '!'

# access each character in the string
for i in range( len(word) ): 
    print ("'%c'" % word[i], end=' ') # access char at index i
print ('')

# output: 'Y' 'e' 's' '!'

##############################################################################

