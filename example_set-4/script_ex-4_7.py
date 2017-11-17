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

## Image manipulation, python package 'PIL'

from PIL import Image
from io import BytesIO
import sys

if len(sys.argv)==2:
    filename = sys.argv[1]
else:
    print ('Usage: %s <input file.jpg>' % sys.argv[0])
    sys.exit(1)

try:
    # open input file (PIL image mode: RGB
    img = Image.open( filename ).convert( 'RGB' )

except IOError as ex:
    print ('error:', ex)
    sys.exit(1)

buf = BytesIO()                # create a string I/O buffer
img.save( buf, format='JPEG' ) # save image (JPEG format) to string I/O buffer
jpeg_data = buf.getvalue()     # read data bytes from string buffer
print (type(jpeg_data))        # show type of jpeg_data
print (len(jpeg_data), 'bytes')
buf.close()

buf = BytesIO()                # create a string I/O buffer
buf.write( jpeg_data )         # write data bytes into string I/O buffer
buf.seek(0)                    # rewind (goto the start position)
img = Image.open( buf )        # open PIL image from the string I/O buffer
img.save( 'copy.jpg', 'JPEG' ) # save PIL image to file
buf.close()

print ('Done...')
sys.stdout.flush()
##############################################################################
