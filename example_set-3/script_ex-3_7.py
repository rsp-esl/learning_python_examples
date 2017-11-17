#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import threading, time
import sys

if sys.version[0] == '2':
    import Queue as queue
else:
    import queue as queue

class Producer(threading.Thread): # the Producer class
    def __init__(self, id, lock, fifo): # constructor
        threading.Thread.__init__(self) # call the superclass constructor
        self.id = id       # set thread ID
        self.lock = lock   # set the mutex lock
        self.fifo = fifo   # set the FIFO for communication

    def run(self): # override: the run() method
        for i in range(10):   # repeat for 10 times
            with self.lock:   # access to the mutex lock
                print ('[Producer id=%d (send: %d)]' % (self.id, i))
            fifo.put( '%d' % i ) # put data (string) to FIFO
            time.sleep(0.1)   # sleep for 0.1 seconds

class Consumer(threading.Thread):
    def __init__(self, id, lock, fifo): # constructor
        threading.Thread.__init__(self)  # call the superclass constructor
        self.id = id       # set thread ID
        self.lock = lock   # set the mutex lock
        self.fifo = fifo   # set the FIFO for communication

    def run(self): # override: the run() method
        while True:
            data = None
            try:
                data = fifo.get(block=False) # get data from FIFO (if any)
            except (queue.Empty): pass  # FIFO is empty 
            else:
                with self.lock: # access to the mutex lock
                    print ('[Consumer id=%d (recv: %s)]' % (self.id, data))
                    if data == '9': break

if __name__ == '__main__': # test code
    fifo = queue.Queue() # create a Queue object (used as FIFO)
    lock = threading.Lock()  # create a mutex lock
    p = Producer(0, lock, fifo) # create a Producer object
    c = Consumer(1, lock, fifo) # create a Consumer object
    p.start()  # start the Producer’s thread
    c.start()  # start the Consumer’s thread
    p.join()   # wait until Producer’s thread exits
    c.join()   # wait until Consumer’s thread exits
    print ('Done....')

# Sample Output:
#    [Producer id=0 (send: 0)]
#    [Consumer id=1 (recv: 0)]
#    [Producer id=0 (send: 1)]
#    [Consumer id=1 (recv: 1)]
#    [Producer id=0 (send: 2)]
#    [Consumer id=1 (recv: 2)]
#    [Producer id=0 (send: 3)]
#    [Consumer id=1 (recv: 3)]
#    [Producer id=0 (send: 4)]
#    [Consumer id=1 (recv: 4)]
#    [Producer id=0 (send: 5)]
#    [Consumer id=1 (recv: 5)]
#    [Producer id=0 (send: 6)]
#    [Consumer id=1 (recv: 6)]
#    [Producer id=0 (send: 7)]
#    [Consumer id=1 (recv: 7)]
#    [Producer id=0 (send: 8)]
#    [Consumer id=1 (recv: 8)]
#    [Producer id=0 (send: 9)]
#    [Consumer id=1 (recv: 9)]
#    Done....
##############################################################################
