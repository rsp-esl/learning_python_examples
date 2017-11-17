#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Random number generation, random package

import random   # import random module

# create a pseudo-random number
x = random.random() # float between [0,1.0)
print ('x is ',end='')
if ( x < 0.5 ):
    print ("Low.")
else:
    print ("High.")

y = random.choice( range(1,10) ) # int between [1,10)
print ('y=', y)

z = random.randint( 1,10 ) # int between [1,10)
print ('z=', z)

##############################################################################
