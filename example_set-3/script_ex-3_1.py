#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import counter

c = counter.Counter()     # create an object from the Counter class
c.incr()                  # increment the counter
counter.Counter.incr( c ) # the same as above
c.reset()                 # reset the counter
for i in range(5):
    c.incr()
    print (c)

print ('-'*20)

from counter import Counter

c = Counter()       # create an object from the Counter class
c.incr()            # increment the counter
Counter.incr( c )   # the same as above
c.reset()           # reset the counter
for i in range(5):
    c.incr()
    print (c)

print ('-'*20)

# Sample output:
#    count = 1
#    count = 2
#    count = 3
#    count = 4
#    count = 5
#    --------------------
#    count = 1
#    count = 2
#    count = 3
#    count = 4
#    count = 5
#    --------------------

##############################################################################
