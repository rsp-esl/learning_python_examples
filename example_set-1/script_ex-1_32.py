#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## try-except structure

# try-except for exception handling in Python
while True:
    try:
        number = int(input("Please enter a number: "))
        break  # if input is ok, exit the while loop

    except ValueError:
        print ("No valid number! Please try again...")

print ('input = ' + str(number))

##############################################################################

