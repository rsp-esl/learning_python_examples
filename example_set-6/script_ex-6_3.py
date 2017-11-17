#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Ubuntu/Linux: 
##  sudo apt-get install -y python-tk python3-tk

## Python Tkinter graphical programming

import sys, math

if (sys.version_info > (3, 0)): # Python 3
   from tkinter import *
else:     # Python 2
   from Tkinter import *

root = Tk() # create a root window from Tkinter.Tk()
root.title( '2D Plot' )
canvas = Canvas( root, width=600, height=400, bg='white' )
canvas.pack()
canvas.create_line( [0,200,600,200], width=2, fill='blue' ) 
canvas.create_line( [300,0,300,400], width=2, fill='blue' ) 
points = []
N = 300
for i in range(-N,N):
    y = int(120*math.sin( 2*math.pi*i/N )) 
    points.append( i + 300 )
    points.append( 200 - y )
    
canvas.create_line( points, width=2, smooth='true', fill='green' ) 
canvas.create_rectangle( [3,3,600,400], width=2, outline='blue' )
root.mainloop() # enter main loop

##############################################################################
