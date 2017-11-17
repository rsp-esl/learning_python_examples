#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

from counter import Counter, UpdownCounter

c = UpdownCounter() # create an object from UpdownCounter
for i in range(3):
    c.incr(), print (c)
for i in range(3):
    c.decr(), print (c)

print (c.count)  # access to the instance variable of the object

# Sample output:
#    count = 1
#    count = 2
#    count = 3
#    count = 2
#    count = 1
#    count = 0
#    0
##############################################################################

