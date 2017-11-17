#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Data types

x = int( "101", 2 )   # convert string (base 2) to int, output: x = 5
print ("x = " + str(x) )

y = int( "101", 10 )  # convert string (base 10) to int, output: y = 101
print ("y = " + str(y))

z = float( "1.23456E+2" ) # convert string to float
t = bool( 0 )    # convert 0 to boolean
c = ord( 'A' )   # convert char to int
c = chr( c + 1 ) # convert int to char

# print formatted string, output: 123.456 101 False 'B'
print ("%.3f %i %s '%c'" % (z, y, t, c)) 

##############################################################################
