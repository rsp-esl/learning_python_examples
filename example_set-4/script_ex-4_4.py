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
import os

# generate thumbnails for image files
def make_thumbnails( path, ext_list=['.jpg'] ):
    try:
        ext_set = set( ext_list )
        for f in os.listdir( path ):
            name, ext = os.path.splitext( f )
            if ext not in ext_set or name.endswith( '_t' ):
                continue  # skip 
            img = Image.open( os.path.join(path,f) ) # open file
            w,h = img.size  # get image width and height
            small_img = img.resize( (int(w/5), int(h/5)) )  # resize -> 20%
            f = os.path.join( path, name + '_t' + ext )
            small_img.save( f )  # save thumbnail as a new file
            print ('generate thumbnail:', f)
    except Exception as err:
        print (err)

images_path = './'

make_thumbnails( images_path ) # specify your path.

##############################################################################
