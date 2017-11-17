#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import time # needed for time.clock()

from to_hex import *  # see file: to_hex.py

t1 = time.clock() # make a timestamp 1
for i in range(0, 200000):
    to_hex(i)

t2 = time.clock() # make a timestamp 2
print ('{:.3f} sec'.format(t2-t1))

t1 = time.clock() # make a timestamp 1
for i in range(0, 200000):
    to_hex2(i)
t2 = time.clock() # make a timestamp 2
print ('{:.3f} sec'.format(t2-t1))

# sample output: 
# 0.478 sec
# 0.304 sec

##############################################################################

