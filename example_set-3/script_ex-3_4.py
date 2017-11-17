#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

from node import Node

if __name__ == '__main__': # test code
    head = None
    for i in range(1,6):
        if head == None:
            head = Node(i) # create a new Node object as the head
        else:
            n = head  # start at the head node
            while n.hasNext(): # goto the last node
                n = n.getNext()
            n.setNext( Node(i) ) # append a new Node object
    n = head             # start at the head node
    while n != None:     # visit each node
        print (n)        # print this node
        n = n.getNext()  # move to the next node

# Output:
#    node 1
#    node 2
#    node 3
#    node 4
#    node 5

##############################################################################

