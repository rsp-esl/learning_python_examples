#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

# Any function containing a yield statement is a generator function.
# A generator function returns an iterator.
def generate_numbers( n ):
    i = 0
    while i < n:
        yield i  # return the next number
        i += 1

print (list( generate_numbers( 5 ) ))
print (sum( generate_numbers( 5 ) ))
print (min( generate_numbers( 5 ) ))
print (max( generate_numbers( 5 ) ))

g = generate_numbers(3) # g is an iterator.
try:
    while True:
        value = next(g)
        if value == None: break
        print ('next:', value)
except (StopIteration) as ex:
    pass

# Output:
#    [0, 1, 2, 3, 4]
#    10
#    0
#    4
#    next: 0
#    next: 1
#    next: 2

##############################################################################
