#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Ubuntu/Linux: 
##  sudo apt-get install -y python-tk python3-tk

## Python Tkinter graphical programming

import sys

if (sys.version_info > (3, 0)): # Python 3
   from tkinter import *
else:     # Python 2
   from Tkinter import *

root = Tk() # create a root window from Tkinter.Tk()
root.title( 'Multiple Canvas' ) # set window title
# create four canvases
canvas1 = Canvas( root, width=320, height=200, bg='light green' )
canvas2 = Canvas( root, width=320, height=200, bg='light blue' )
canvas3 = Canvas( root, width=320, height=200, bg='yellow' )
canvas4 = Canvas( root, width=320, height=200, bg='pink' )
canvas1.grid( row=0, column=1 )
canvas2.grid( row=0, column=0 )
canvas3.grid( row=1, column=0 )
canvas4.grid( row=1, column=1 )

root.mainloop() # enter main loop

##############################################################################

