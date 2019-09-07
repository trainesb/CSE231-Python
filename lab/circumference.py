# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:43:18 2017

@author: Ben
"""

import math

radiusString = input ("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print ("The cirumference is:",circumference , \
", and the area is:",area)