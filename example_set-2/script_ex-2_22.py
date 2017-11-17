#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

class X:
    name  = "class X" # class variable
    count = 0         # class variable
    def __init__(self, name): # constructor
        self.name = name  # set instance variable
    def __str__(self): # override
        return X.name + ': ' + self.name
    def __next__(self):
        X.count = X.count + 1
        return X.count
    def next(self):
        return self.__next__()

if __name__ == '__main__': # test code
    print (X.name)
    obj_1 = X("object1") # create an object from class X
    print (obj_1)
    obj_2 = X("object2") # create an object from class X
    print (obj_2)
    print (obj_1.next())
    print (obj_1.next())
    print (obj_2.next())
    print (obj_2.next())

# Output:
#    class X
#    class X: object1
#    class X: object2
#    1
#    2
#    3
#    4

##############################################################################

