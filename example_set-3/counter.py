#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

class Counter:
    def __init__(self): # default constructor
        self.reset()    # call the member method: reset()
    def reset(self):    # reset the member field: counter
        self.count = 0  # reset the instance variable ‘count’
    def incr(self):     # increment the counter
        self.count = self.count + 1
    def __str__(self):  # override the __str__ method
        return 'count = %d' % self.count

# The UpdownCounter class extends the Counter class.
class UpdownCounter(Counter):
    def __init__(self):     # default constructor
        # call the constructor of its superclass
        Counter.__init__(self) 
    def decr(self):         # decrement the counter
        if (self.count > 0):
            self.count = self.count-1

if __name__ == '__main__': # test code
    c = Counter() # create an object from the Counter class
    c.incr()
    print (c)

##############################################################################

