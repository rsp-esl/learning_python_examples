#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

listA = [1,2,-1,3,-2,-4,0,-3,4,5]

# create a new list from listA, but only elements with non-negative values
listB = [x for x in listA if (x >= 0)] 
print ('listB =',listB)

# output: listB = [1, 2, 3, 0, 4, 5]

listC = list( set(listA) - set(listB) )
print ('listC =',listC)

# output: listC = [-2, -4, -3, -1]

##############################################################################
