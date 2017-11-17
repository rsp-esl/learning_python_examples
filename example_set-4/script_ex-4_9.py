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
from PIL import Image

host = '127.0.0.1'     # the remote IP address of your UDP Server
port = 8000            # remote port

sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # create a socket
sock.settimeout( 5 )        # timeout in seconds
sock.connect( (host,port) ) # connect to the UDP server 

print ('UDP client started..',flush=True )
count = 1
while True:
    try:
        sock.send( ('request #%d' % count).encode() )
        (received, addr) = sock.recvfrom( 65535 ) # max. size = 65535 bytes
        print ("Received: %d bytes" % len(received))
        print ("From:     %s" % str(addr))

        buf = BytesIO()      # create a bytes I/O buffer
        buf.write( received )   # write received bytes to the String I/O buffer
        buf.seek(0)             # rewind the String I/O buffer
        img = Image.open( buf ) # open PIL image from the String I/O buffer
        img.save( 'received-%d.jpg' % count, 'JPEG' ) # save to output file
        buf.close()

        count = count + 1
        if count > 5: 
             break
        time.sleep(5.0)         # wait for 5 seconds

    except KeyboardInterrupt as ex:
        sys.exit(1)

##############################################################################
