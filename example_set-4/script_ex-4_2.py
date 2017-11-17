#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

##############################################################################
## Install the Pillow (instead of PIL) package
## pip  install pillow -U
## pip3 install pillow -U
##############################################################################

## Image manipulation, Python package 'PIL'

from PIL import Image
import sys

if len(sys.argv) == 3:
   inputs = (sys.argv[1], sys.argv[2])
else:
   print ('Usage: %s <input1> <input2>' % sys.argv[0])
   sys.exit(-1)

size = (640,480) 
Img  = Image.new( 'RGBA', size ) # create a blank image, 640x480, RGBA mode
img1 = Image.open( inputs[0] )   # open input file 1
img2 = Image.open( inputs[1] )   # open input file 2
img3 = Image.blend( img1, img2, alpha=0.50 ) # perform alpha-blending

img.paste( img3, (0,0) )         # paste image on blank image at position (0,0) 
img.save( 'output4-2.jpg' )      # save the result to output file

print ('Done...')
##############################################################################
