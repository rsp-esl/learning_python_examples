#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Python package 'datetime'

import datetime

now = datetime.datetime.now() # get current date & time
print (now.ctime())
print (now.strftime( "%Y-%m-%d, %H:%M:%S" ))

d = now.date()     # get current date
print ('%d-%02d-%02d' % (d.year, d.month, d.day))

t = now.time()     # get current time (timestamp)
print ('%02d:%02d:%02d' % (t.hour, t.minute, t.second))

today = datetime.date.today()
print (today)

# sample output:
#   Sun Mar 15 11:38:42 2015
#   2015-03-15, 11:38:42
#   2015-03-15
#   11:38:42
#   2015-03-15

now   = datetime.datetime.now()
start = datetime.datetime(1970,1,1)
print ( (now - start).total_seconds() ) # get time in seconds since 1/1/1970

##############################################################################

