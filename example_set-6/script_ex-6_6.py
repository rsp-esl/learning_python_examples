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
# create canvas Widget for drawing
canvas = Canvas( root, width=600, height=400, bg="white" )
canvas.grid( row=0, column=0 ) # use the grid layout manager
# create a line (x1, y1, x2, y2)
canvas.create_line( 100,200,400,200, width=10, fill="red" )
# create a polygon (x1,y1, x2, y2, .... )
points = [400,150, 500,200, 400,250] # list of points
canvas.create_polygon( points, fill="red" ) 
# create a dash line (x1, y1, x2, y2)
canvas.create_line( 100,300, 500,300, dash=(5,3), width=5,
                   caps="round", fill="grey" )
root.mainloop() # enter main loop 

##############################################################################
