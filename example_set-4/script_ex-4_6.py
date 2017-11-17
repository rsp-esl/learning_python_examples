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

from PIL import Image

filename = 'input.jpg'

try:
    img = Image.open( filename ) # open input (JPEG) file
    width, height = img.size  # get size of the original image
    bbox = [150, 150, width-150, height-150]

    img = img.crop( bbox ) # crop the image
    
    width, height = img.size  # get size of the cropped image
    img = img.resize( (int(width/2), int(height/2)) ) # reduce size 50%
    img.save( 'output4-6.jpg' ) # save to output file
    print ('Done...')

except Exception as err:
    print (err)

##############################################################################

