#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Lists, Dictionaries

x = 10
y = 20
num_list = [x]                # create a new list with one element (int)
num_list.append( y )          # append an integer to the list
print ('num_list = ', num_list)   # output: num_list= [10, 20]


num_tuple = (30,40,50)        # create a tuple of integers
num_list += list( num_tuple ) # append a tuple to the list
print ('num_list = ', num_list)   # output: num_list= [10, 20, 30, 40, 50]

import itertools

# merge all elements from lists into a new list.
lists = [['a'], ['b', 'c'], ['d', 'e', 'f']]
new_list = [i for i in itertools.chain.from_iterable(lists) ]
print ('new_list = ', new_list)   # output: new_list= ['a', 'b', 'c', 'd', 'e', 'f']

listA = [1, 2, 3, 4, 5]
listB = ["red", "blue", "orange", "black", "grey"]
d = dict(zip(listA, listB))   # create a dictionary from two lists (keys and values)
for key in d:
    print (key,'=>',d[key])

# output: 
#  1 => red
#  2 => blue
#  3 => orange
#  4 => black
#  5 => grey

##############################################################################

