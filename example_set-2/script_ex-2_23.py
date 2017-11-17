#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

s = '1:22:333:4444:'
i = 0
results = []
while True:
    j = s.find( ':', i )
    if j == -1:
        results.append( s[i:] )
        break
    results.append( s[i:j] )
    i = j+1

print (results)
print (s.split(':')) # split a string into a list of substrings

# Output:
#    ['1', '22', '333', '4444', '']
#    ['1', '22', '333', '4444', '']

##############################################################################

