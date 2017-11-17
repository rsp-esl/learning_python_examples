#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Class definitionin python

class Flag:   # define a class

    def __init__(self):            # default constructor
    	self.state = False

    def __init__(self,initState):  # constructor
    	self.state = initState

    def turnOn(self):
    	self.state = True

    def turnOff(self):
        self.state = False

    def __str__(self):             # a toString() method
        return "[" + str(self.state) + "]"


f = Flag(False)  # create an object from the Flag class

f.turnOn();  
print (f)          # output: [True]

f.turnOff(); 
print (f)          # output: [False]

##############################################################################

