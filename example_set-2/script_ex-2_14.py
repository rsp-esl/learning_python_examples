#!/usr/bin/env python

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import os.path

path = '/home/rsp/Downloads/file.tar.gz'
file = os.path.basename(path)
print ('file = "%s"' % file)
dir = os.path.dirname(path)
print ('dir = "%s"' % dir)

pos = path.rfind('/')
file = path[pos+1:]
if len(file) > 0:
    print ('file = "%s"' % file)

results = os.path.splitext( path )
print (results)

fileName, fileExtension = os.path.splitext( path )
print (fileName, fileExtension)

# Output:
#    file = "file.tar.gz"
#    dir = "/home/rsp/Downloads"
#    file = "file.tar.gz"
#    ('/home/rsp/Downloads/file.tar', '.gz')
#    /home/rsp/Downloads/file.tar .gz

##############################################################################

