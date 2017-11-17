#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

import os

path_names = [ '..' ]

levels = 3  # limit to 3 levels deep

while len(path_names) > 0 and levels > 0:
    new_path_names = []
    for path_name in path_names:
        if path_name[-1] == '/':
           path_name = path_name[:-1]  # remove the last '/' in the string
           
        try:
            print ('>', path_name) # show directory name
            for name in os.listdir( path_name ):
                _name = path_name + '/' + name
                if os.path.isdir( _name ):
                    new_path_names.append( _name )
        except Exception as err:
            print ('Cannot access:', path_name, err)

    path_names = []

    levels -= 1

    if len(new_path_names) > 0:
        path_names.extend( new_path_names )

print ('Done...')

##############################################################################

