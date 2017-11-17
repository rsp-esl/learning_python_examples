#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Ubuntu/Linux: 
##  sudo apt-get install -y python-tk python3-tk

## Python Tkinter graphical programming

import sys, math, random, time

if (sys.version_info > (3, 0)): # Python 3
   from tkinter import *
else:     # Python 2
   from Tkinter import *

root = Tk() # create a root window from Tkinter.Tk()
root.title( 'Animation' ) # set window title
canvas = Canvas( root, width=640, height=480, bg='white' )
canvas.grid( row=0, column=0 )
xpos = 320
ypos = 240
colors = ['red', 'lightgreen', 'blue', 'yellow', 'cyan' ]
for i in range(1,200):
     xpos = (200-i)*math.cos( math.pi*i/50 ) + 320
     ypos = (200-i)*math.sin( math.pi*i/50 ) + 240
     canvas.create_oval(
        [xpos-5, ypos-5, xpos+5, ypos+5], outline='black',
        fill=colors[ random.randint(0, len(colors)-1) ] )
     canvas.update() # refresh the drawing on the canvas.
     canvas.after( 100 ) # make execution pause for 100 msec
     #canvas.delete(ALL) # Clear everything on the canvas
     
root.mainloop()

##############################################################################
