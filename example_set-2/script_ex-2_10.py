#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Python packages 'os' and 'sys'
## Directory listing

import os, sys

print ('Your platform is %s.' % (sys.platform))

pathname = './' 
names = os.listdir( pathname ) # directory listing
for name in names: 
    if not os.path.isdir( pathname + name ):
        base, ext = os.path.splitext( name )

        # show only files with the following extensions
        if ext in set(['.py','.txt']):
            filename = pathname + name
            print ('File: "%s"' % (filename))

##############################################################################

