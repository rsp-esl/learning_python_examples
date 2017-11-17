#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

## Binary string and conversion

x = 122; y = 0x0f # two variables with integer values  
print ('x =', x, '(dec) =', hex(x),
    '(hex) =', bin(x), '(bin)')

# output: x = 122 (dec) = 0x7a (hex) = 0b1111010 (bin)

b = bin((x>>4) & y)      # bitwise right-shift, AND mask
print (b)                # print (binary) string            : 0b111
print ((b[2:]).zfill(8)) # fill with leading 0's, 8 pos.    : 00000111

y = '0xfe'
b = bin(int(y, 16)) # convert hex to bin (string)
print (b)        # show binary string                       : 0b11111110
print (b[2:])    # show binary string, but no leading '0b'  : 11111110

##############################################################################

