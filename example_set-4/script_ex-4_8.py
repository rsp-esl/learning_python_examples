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

## Image manipulation, Python package 'PIL', Socket programming

import socket, sys, time
from io import BytesIO
import socketserver
from PIL import Image

## UDP Server class
class MyUDPHandler(socketserver.BaseRequestHandler):    
    def handle(self): # called upon request from UDP client
        (data,sock) = self.request
        filename = 'input_small.jpg'  # default image file
        print ('received request from %s:' % str(self.client_address))
        print ('%s' % str(data.decode()) )
        img = Image.open( filename ).convert( 'RGB' ) # open PIL image from file
        buf = BytesIO()
        img.save( buf, format='JPEG' )
        jpeg_data = buf.getvalue()
        print (len(jpeg_data), 'bytes sent')
        buf.close()
        sock.sendto( jpeg_data, self.client_address ) # send data to client

if __name__ == "__main__":
    try:
        print ('UDP Server started...')
        host, port = '', 8000  # use UDP port = 8000
        # create a Socket Server and use it with MyUDPHandler
        server = socketserver.UDPServer((host,port), MyUDPHandler)
        server.serve_forever( poll_interval=0.5 )

    except KeyboardInterrupt as ex:
        sys.exit(1)
    else:
        print ('UDP Server stopped...')

##############################################################################

