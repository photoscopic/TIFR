# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 19:50:35 2022

@author: parab
"""

from scipy.interpolate import CubicSpline
def cubicinter(l):
 x=[0,1,2]
 y =[1,2,4]
 f = CubicSpline(x, y)
 return f(l)
x=1.5
print('value from cubic interpolation:',cubicinter(x))
print('actual value is:',2**(1.5))
