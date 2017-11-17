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
root.title( 'Basic 2D graphics in Tkinter' ) # set window title
root.geometry( "600x400+200+100" ) # set window size and position
# create canvas Widget for drawing
canvas = Canvas( root, width=600, height=400, bg="#ffffff" )
canvas.grid( row=0, column=0 ) # use the grid layout manager

# create a oval (ellipse) within a bounding box = (x1, y1, x2, y2)
canvas.create_oval( [150,50, 450,350], fill="yellow" )
# create an arc with in a bounding box (x1, y1, x2, y2)
canvas.create_arc( [150,50, 450,350],
                   start=0.0, extent=45.0, fill="light green" )
root.mainloop() # enter main loop

##############################################################################

