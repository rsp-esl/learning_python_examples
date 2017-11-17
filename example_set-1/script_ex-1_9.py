#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Loop

# while loop
x = 0  # initialize loop variable
n = 20
while (x < n):
    if not( (x % 2 == 0) or (x % 3 == 0) ):
         print (x, end=' ') # print the value of x, without newline
    x = x+1       # increment x
print ('')

## for loop
for x in range(n):
    if not( (x % 2 == 0) or (x % 3 == 0) ):
         print (x, end=' ') # print the value of x, without newline
print ('')

# output: 1 5 7 11 13 17 19 

n = 10
for i in range(1,n):
    print (i*i, end=' ') # print the value of i*i, without newline
print ('')

# output: 1 4 9 16 25 36 49 64 81

for i in range( n ):
    print (i*i, end=' ') # print the value of i*i, without newline
print ('')

# output: 0 1 4 9 16 25 36 49 64 81

for i in [1,2,3,4,3,2,1]:
    print ('#'*(i))

n=5
for i in [ n-abs(x) for x in range(-n+1,n) ]:
    print ('*'*(i))

##############################################################################
