#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()

class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()

##############################################################################

y = yrange(5)

try:
  for i in range(10):
     print ('next(y):', next(y)) # the same as y.next()
except StopIteration:
  pass

print ('y =', list(y))  # this is an empty list.
print ('-'*20)

print (list( yrange(5) ))
print (sum( yrange(5) ))

print ('-'*20)

##############################################################################

z = zrange(5)
print (list( z ))
print (sum( z ))

print ('z =', list(z))  # the list is not empty.
print ('-'*20)

# Output:
#    next(y): 0
#    next(y): 1
#    next(y): 2
#    next(y): 3
#    next(y): 4
#    y = []
#    --------------------
#    [0, 1, 2, 3, 4]
#    10
#    --------------------
#    [0, 1, 2, 3, 4]
#    10
#    z = [0, 1, 2, 3, 4]
#    --------------------
##############################################################################
