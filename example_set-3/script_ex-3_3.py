#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

class Point2d:
    def __init__(self,x=0,y=0): # constructor
        self.set(x,y)
    def set(self,x,y):
        self.x = x
        self.y = y
    def __str__(self): # override: convert to string
        return '(%.3f,%.3f)' % (self.x, self.y)

if __name__ == '__main__': # test code
    p1 = Point2d(x=1,y=-1)
    p2 = Point2d()
    p2.set(-1, 1)

    Point2d.set( p2, -1, 1 ) # the same as above

    p3 = Point2d(2,3)
    p4 = Point2d()
    p4 = p3

    for p in [p1, p2, p3, p4]: print (p)
    setattr(p1,'x',0) # access to p1.x to set a new value
    setattr(p1,'y',2) # access to p1.y to set a new value
    print ('p1.x =', getattr(p1,'x')) # access to p1.x to get the value
    print ('p1.y =', getattr(p1,'y')) # access to p1.y to get the value

# Output:
#    (1.000,-1.000)
#    (-1.000,1.000)
#    (2.000,3.000)
#    (2.000,3.000)
#    p1.x = 0
#    p1.y = 2

##############################################################################

