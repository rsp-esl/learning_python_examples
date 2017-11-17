#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import random
import functools

numbers = [ random.randint(-10,10) for x in range(10) ]
print (numbers)

# Apply reduce() to lambda constructs
print ('min =', functools.reduce( lambda x,y: min(x,y), numbers )) # get min value 
print ('max =', functools.reduce( lambda x,y: max(x,y), numbers )) # get max value
print ('min =', min( numbers )) # get min value
print ('max =', max( numbers )) # get max value

print ('absolute values:', list(map( abs, numbers ))) # get absolute values

# Sample Output (depending on randomized values):
#   [4, 0, -5, 2, 6, 4, -5, -2, 9, -4]
#   min = -5
#   max = 9
#   min = -5
#   max = 9
#   absolute values: [4, 0, 5, 2, 6, 4, 5, 2, 9, 4]

##############################################################################

