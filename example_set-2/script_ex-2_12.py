#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

# open a new file named 'out.txt', overwrite the file if it exists.
filename = 'data.txt'
f = open( filename, 'w' ) # open a text file in write mode 

for i in range(1,5):     # 1, 2, 3, 4
    f.write( str(i) + '\n' ) # write a text line to file
f.close()

f = open( filename, 'r' ) # open a text file in read mode
while True:
    t = f.readline().strip() # read the next line
    if len(t) == 0: # empty string
        break       # exit loop (end of file)
    print ('>', t)  # show the current text line
f.close()

print ('Done...' )

##############################################################################
