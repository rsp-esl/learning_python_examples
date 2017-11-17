#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Python packages: os and sys 
## path scanning, directory listing

import os, sys # import modules os and sys

print ('platform = ', sys.platform) # print the platform's name
path = '.'  # set current path
ext = '.py' # set file extension for Python 
filelist = [] # create an empty list

for filename in os.listdir( path ):
    if filename.endswith( ext ):
        filelist.append( filename )
for f in filelist: # show list of Python script file(s)
    print (f)
    
##############################################################################

