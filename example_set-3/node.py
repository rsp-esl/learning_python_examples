#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

class Node:
    def __init__(self, data, nextNode=None): # constructor
        self.data = data
        self.next = nextNode
    def getNext(self):
        return self.next
    def setNext(self, node):
        self.next = node
    def hasNext(self):
        return (self.next != None)
    def __str__(self): # override: convert to string
        return 'node %s' % str(self.data)

if __name__ == '__main__': # test code
    p = None
    for i in range(5):
        p = Node(i, p)	# create a new Node object
    n = p
    while n != None:
        print (n)
        n = n.getNext()

##############################################################################

