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

# specify the input and output filenames 
input_photo  = 'input.jpg'
output_photo = 'output4-1.jpg'

img = Image.open( input_photo ) # open image from the input file
img.load()                # load image now

#img = img.rotate( 90 )   # rotate image counter-clockwise, 90 degree
img_w, img_h = img.size   # get image dimension

img = img.resize( (int(img_w/4), int(img_h/4)), Image.ANTIALIAS ) # resize image -> 25%

img.save( output_photo )        # save image to output file

print ('Done...')
sys.stdout.flush()

##############################################################################

