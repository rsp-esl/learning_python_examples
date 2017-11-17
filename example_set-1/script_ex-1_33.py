#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## try-except structure, exception handling

import sys # needed for sys.exit and sys.stderr

try: # read one or more numbers from standard input
    inputs = input('Enter number(s) (separated with commas): ')
    if isinstance(inputs, (str)):
        numbers = tuple( map(float,inputs.split(',')) )
except (ValueError): 
    sys.stderr.write( 'Input is not a number! \n' )
    sys.stderr.write( 'Program exited...\n' )
    sys.exit(-1) # stop execution
else:

    print ('input =', numbers)    # print numbers
    print ('sum =', sum(numbers)) # calculate sum
    print ('min =', min(numbers)) # find min value
    print ('max =', max(numbers)) # find max value
    print ('sorted =', sorted(numbers)) # sort the list
finally:
    print ('Done...')

##############################################################################
