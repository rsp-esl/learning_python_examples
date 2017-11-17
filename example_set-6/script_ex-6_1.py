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

root = Tk() # create a root (main) window from Tkinter.Tk()
root.title( 'Basic 2D graphics' ) # set window title

# create canvas Widget for drawing
canvas = Canvas( root, width=640, height=480, bg="#ffffff" )
canvas.grid( row=0, column=0 ) # use the grid layout manager

for i in range(1,10):
    # create a rectangle (x1, y1, x2, y2)
    canvas.create_rectangle( 10*i, 10*i, 640-10*i, 480-10*i,
                             width=i, outline="blue" )
root.mainloop() # enter main loop

##############################################################################
