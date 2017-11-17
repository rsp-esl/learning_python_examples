#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## class definition, multi-threading

import threading, time, sys

# MyTask is a subclass of Thread.
class MyTask(threading.Thread):
    def __init__(self, name):  # constructor
        threading.Thread.__init__(self)
        self.name  = name
        self.count = 0
        
    def run(self): # overriding the run method()
        while True:
            time.sleep(0.5) # sleep for 0.5 seconds
            if self.count > 10:
                print (self.name, 'finished...')
                break
            print (self.name,'count:', self.count)
            sys.stdout.flush()
            self.count += 1

task = MyTask('MyTask')  # create an object from MyTask

task.start()  # start the task
print ('Waiting for task termination...')

task.join()
print ('Done....')

# Sample Output:
#    Waiting for task termination...
#    MyTask count: 0
#    MyTask count: 1
#    MyTask count: 2
#    MyTask count: 3
#    MyTask count: 4
#    MyTask count: 5
#    MyTask count: 6
#    MyTask count: 7
#    MyTask count: 8
#    MyTask count: 9
#    MyTask count: 10
#    MyTask finished...
#    Done....

##############################################################################
