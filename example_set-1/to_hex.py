#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Function, integer to hex string conversion

def to_hex( value ):
    digits = []
    HEX_DIGITS = '0123456789abcdef'
    if (value < 0):
        value += (1 << 32) # 32-bit value
    while True:
        x = (value & 0xf)
        digits.insert( 0, HEX_DIGITS[x] )
        value >>= 4
        if value == 0:
            break
    s = '0x'
    for digit in digits:
        s += digit
    return s

def to_hex2( value ):
    HEX_DIGITS = '0123456789abcdef'
    s = ''
    if (value < 0):
        value += (1 << 32)  # 32-bit value
    while True:
        d = HEX_DIGITS[ value & 0xf ]
        s = d + s
        value >>= 4
        if value == 0:
            break
    s = '0x' + s
    return s

if __name__ == "__main__":
    print (to_hex(33))  # 0x21
    print (to_hex(-1))  # 0xffffffff
    print (to_hex2(33))  # 0x21
    print (to_hex2(-1))  # 0xffffffff

##############################################################################

