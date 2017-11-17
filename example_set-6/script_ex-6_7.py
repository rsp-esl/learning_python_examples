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
text_str = 'I Love Python!'
for i in range(1,10): 
    text_font = ( 'Times', 10 + i*2 ) # create text font
    # draw text at (x,y) using the specified text font and fill color
    canvas.create_text( (300, 30*(i+1)), anchor=NE,
                        text=text_str, fill='blue', font=text_font )
    canvas.create_text( (300, 30*(i+1)), anchor=NW,
                         text=text_str, fill='green', font=text_font )
root.mainloop()

##############################################################################
