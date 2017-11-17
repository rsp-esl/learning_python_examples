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

filename = 'input.jpg'  #  The input file is located in the same directory.

try:
    img = Image.open( filename ) # open input (JPEG) file
    width, height = img.size
    print (width, height)  # show image width and height
    img_gray = img.convert('L')   # convert to grayscale
    img_gray.save( 'output4-5.jpg' ) # save to output file
    print ('Done...')

except (Exception) as ex:
    print (ex)

##############################################################################
