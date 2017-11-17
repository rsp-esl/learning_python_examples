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

## $ sudo apt-get install python-pil python-tk python-imaging-tk

from PIL import Image, ImageTk # from the PIL library

root = Tk()
canvas = Canvas( root, width=640, height=480 )
canvas.grid( row=0, column=0 )

im = Image.open( 'input.jpg' ) # open image file
im = im.resize( (640,480), Image.ANTIALIAS ) # resize image
photo = ImageTk.PhotoImage( im ) # create Tk image from PIL image
canvas.create_image( 0,0, anchor=NW, image=photo ) # draw image
root.mainloop()

##############################################################################
