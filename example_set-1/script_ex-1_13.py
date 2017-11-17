#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Random number generation, random package

import random # needed for random.ranint() 

scores = []   # create an empty list
for i in range(10): # generate 10 random numbers
    scores.append( random.randint(50,100) )
print (scores)

print ('min = ', min( scores ) ) 
print ('max = ', max( scores )  )

sorted_list = sorted( scores ) # create a sorted list
last = len( sorted_list ) - 1
print ("first element (sorted) = ", sorted_list[0])
print ("last element  (sorted) = ", sorted_list[ last ])

# output:
#  [54, 97, 62, 85, 59, 98, 89, 95, 51, 69]
#  min = 51
#  max = 98
#  first element (sorted) = 51
#  last element  (sorted) = 98

##############################################################################
