#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, List manipulation

list1 = [ 1,2,3 ]   # list1 contains 3 integers
list2 = [ 4,5,6 ]   # list2 contains 3 integers
list3 = list1       # list1 and list3 reference the same list
list3 += list2      # add elements of list2 to list3 

print ('list1 =', list1)
print ('list3 =', list3)

# output:
#   list1 = [1, 2, 3, 4, 5, 6]
#   list3 = [1, 2, 3, 4, 5, 6]

list4 = [] + list2  # create a copy of list2
del list2[0]        # delete the first element from list2

print ('list2 =', list2)
print ('list4 =', list4)

# output:
#   list2 = [5, 6]
#   list4 = [4, 5, 6]

##############################################################################

