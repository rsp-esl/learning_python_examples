#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# Author: Rawat S. (Dept. of Electrical & Computer Engineering, KMUTNB)
# Date: 2017-11-17
##############################################################################

from __future__ import print_function # for Python 2.6 or higher

## Data structures, Dictionaries

# Data structure: create a dictionary
countries = {
  'TH': 'Thailand',
  'DE': 'Germany',
  'FR': 'France' 
}

# add more key-value pairs to the dictionary
countries[ 'UK' ] = 'England'
countries[ 'DK' ] = 'Denmark'
countries[ 'GR' ] = 'Greece'

if 'DE' in countries:
    print (countries['DE'])

print ( ' '.join( [ countries[key] for key in countries.keys()] ) )

##############################################################################
