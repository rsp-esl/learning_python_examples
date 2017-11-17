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

if len(sys.argv)==2:
    filename = sys.argv[1]
    print ('read input "%s"' % filename)
else:
    print ('Usage: %s <file.jpg>' % (sys.argv[0]))
    sys.exit(1)

try:
    img = Image.open( filename ).convert( 'RGB' )
    (img_w,img_h) = img.size       # get image size
    img_mode = img.mode            # get image mode; it should be 'RGB'.
    pixels = img_w * img_h         # number of pixels
    print ('%d x %d = %d pixels' % (img_w, img_h, pixels))

    img_data = img.tobytes()       # convert to pixels data to bytes
    img = Image.frombytes( 'RGB', (img_w, img_h), img_data ) # convert back
    img.save( './output4-3.jpg', 'JPEG' ) # save the copy to file

except IOError as ex:
    print ('error:', ex)

##############################################################################
