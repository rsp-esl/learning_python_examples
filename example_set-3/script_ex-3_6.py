#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import threading, time

# define the MyThread class as a subclass of threading.Thread
class MyThread(threading.Thread):
    def __init__(self, id, lock): # constructor
        # call the constructor of its superclass
        threading.Thread.__init__(self)
        self.id = id       # set thread ID
        self.lock = lock   # set the mutex lock

    def run(self): # override the run method() of its superclass
        for i in range(10):   # repeat for 10 times
            with self.lock:   # access to the mutex lock
                print ('[Thread id=%d (%d)]' % (self.id, i))          
            time.sleep(0.5)   # sleep for 0.5 seconds

if __name__ == '__main__': # test code
    lock = threading.Lock()  # create a mutex lock
    threads = []             # create an empty list
    num_threads = 5          # number of threads to be created
    for i in range(num_threads):
        # create a new thread object
        threads.append( MyThread(i,lock) ); 
    for t in threads:   # for each thread in the list
        # invoke the run() method of this thread
        t.start() 
    for t in threads:   # for each thread in the list
        # the main thread must wait until this thread exits.
        t.join()
    print ('Done...')

# Sample output:
#
#    [Thread id=0 (0)]
#    [Thread id=1 (0)]
#    [Thread id=2 (0)]
#    [Thread id=3 (0)]
#    [Thread id=4 (0)]
#    [Thread id=1 (1)]
#    [Thread id=2 (1)]
#    [Thread id=0 (1)]
#    [Thread id=3 (1)]
#    [Thread id=4 (1)]
#    [Thread id=2 (2)]
#    [Thread id=3 (2)]
#    [Thread id=1 (2)]
#    [Thread id=0 (2)]
#    [Thread id=4 (2)]
#    [Thread id=2 (3)]
#    [Thread id=0 (3)]
#    [Thread id=3 (3)]
#    [Thread id=1 (3)]
#    [Thread id=4 (3)]
#    [Thread id=2 (4)]
#    [Thread id=0 (4)]
#    [Thread id=3 (4)]
#    [Thread id=1 (4)]
#    [Thread id=4 (4)]
#    [Thread id=2 (5)]
#    [Thread id=0 (5)]
#    [Thread id=3 (5)]
#    [Thread id=4 (5)]
#    [Thread id=1 (5)]
#    [Thread id=1 (6)]
#    [Thread id=0 (6)]
#    [Thread id=3 (6)]
#    [Thread id=2 (6)]
#    [Thread id=4 (6)]
#    [Thread id=4 (7)]
#    [Thread id=1 (7)]
#    [Thread id=0 (7)]
#    [Thread id=3 (7)]
#    [Thread id=2 (7)]
#    [Thread id=0 (8)]
#    [Thread id=1 (8)]
#    [Thread id=3 (8)]
#    [Thread id=2 (8)]
#    [Thread id=4 (8)]
#    [Thread id=0 (9)]
#    [Thread id=3 (9)]
#    [Thread id=1 (9)]
#    [Thread id=4 (9)]
#    [Thread id=2 (9)]
#    Done...

##############################################################################
