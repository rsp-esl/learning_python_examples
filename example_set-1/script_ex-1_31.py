#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structure: A tuple is a list like structure
## which cannot be altered after creating it.

x = ['a', 'b', 'c', 'd'] # create a list
t = tuple( x ) # create a tuple from a list
for i in range( len(t) ):
    print (t[i],end=' ')
print ('')

# output: a b c d

# create a list of tuples
numbers = [
    (0,'Sunday'), (1,'Monday'), (2,'Tuesday'), (3,'Wednesday'),
    (4,'Thursday'),(5,'Friday'),(6,'Saturday') ]

print( ' '.join([t[1] for t in numbers]) )

# output: Sunday Monday Tuesday Wednesday Thursday Friday Saturday

##############################################################################
