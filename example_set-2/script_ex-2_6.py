#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, List manipulation

def rotate_left( _list ):
    _list.append( _list.pop(0) )
    return _list

list1 = list(range(0,4)) 
print ('list1 =', list1)
list2 = rotate_left( list1 )
print ('list1 =', list1)
print ('list2 =', list2)

import collections # needed for deque (data structure)

d = collections.deque() # create an empty deque
d.extend( [1, 2, 3, 4] ) # append elements to the deque
for num in range(5,10):
    d.append( num ) # append each element to the deque
d.appendleft( 0 )

print ('First element =', d[0])
print ('Last element  =', d[ len(d)-1 ])
print (d.pop())
print (d.popleft())
print (d)

from collections import deque

d = deque( [1,2,3] )
d.append( 4 )           # add 4 at the last position
d.appendleft( 0 )       # add 0 at the first position
print ('d =', d)

d.append( d.popleft() ) # rotate left
print ('d =', d)

d.rotate()              # rotate right
print ('d =', d)

d.reverse()             # reverse the order
print ('d =', d)

# output:
#    list1 = [0, 1, 2, 3]
#    list2 = [1, 2, 3, 0]
#    First element = 0
#    Last element  = 9
#    9
#    0
#    deque([1, 2, 3, 4, 5, 6, 7, 8])
#    d = deque([0, 1, 2, 3, 4])
#    d = deque([1, 2, 3, 4, 0])
#    d = deque([0, 1, 2, 3, 4])
#    d = deque([4, 3, 2, 1, 0])

##############################################################################
