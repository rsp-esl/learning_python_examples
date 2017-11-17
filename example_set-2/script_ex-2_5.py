#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, List manipulation

def rotate_right( _list ): # define a function
    _list.insert( 0, _list.pop() )
    return _list

# create a list: [10, 20, 30]
list1 = [ 10*(e+1) for e in xrange(3) ]
for i, e in enumerate( list1 ):
    print (i, '->', e)

# output:
#   0 -> 10
#   1 -> 20
#   2 -> 30

list2 = rotate_right( list1 )
print ('list1 =', list1)
print ('list2 =', list2)

# output:
#   list1 = [30, 10, 20]
#   list2 = [30, 10, 20]

##############################################################################

