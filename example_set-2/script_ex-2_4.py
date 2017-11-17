#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, List manipulation

import random

fruits = [ 'Apple', 'Orange', 'Mango',
           'Watermellon', 'Banana' ]

# generate a pseudorandom integer
index = random.randint( 0, len(fruits)-1 )
name = fruits[ index ]

if name not in fruits: # search element in a list
    print ("Not found: " + name)
else:
    print ("Found: " + name)

# list of strings
fruits = [ 'Apple', 'Orange', 'Mango',
           'Watermellon', 'Banana' ]

for name in [ 'Banana', 'Apple', 'Strawberry']:
    try: # find an element in the list
        index = fruits.index( name )
        del fruits[index] # remove it from the list
    except (ValueError):
        print ("Not found: " + name)
    else:
        print ("Removed: " + name)

print (fruits) # show the remaining list

# sample output:
#  Removed: Banana
#  Removed: Apple
#  Not found: Strawberry
#  ['Orange', 'Mango', 'Watermellon']

##############################################################################

