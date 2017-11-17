#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Loop

x = 0  # initialize loop variable
while (x < 20):
    if ((x % 2 == 0) or
        not(x % 3)):
        pass      # do nothing (skip)
    else:
        print x, # print x
    x = x+1       # increment x
print ''

# output: 1 5 7 11 13 17 19 

##############################################################################
