#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

try:
    line_num = 1
    fin = open( 'data.txt', 'r' ) # open input text file for read-only
    line = fin.readline() # read the first line

    while ( line != '' ):
        print ('[%03i]' % line_num, line.strip())  # show text with line number
        line = fin.readline() # read the next line
        line_num += 1

    print ('--------------')

    fout = open( 'output.txt', 'w' ) # open text file for write
    fin.seek( 0 ) # go back to the start of file
    lines = fin.readlines() # read multiple text lines from input file

    for i, line in enumerate(lines):
        print ('[%03d]' % i, line.strip())
        fout.write( line )
    fin.close()
    fout.close()
 
except (Exception) as ex:
    print ('Error:', ex)
    pass

##############################################################################
