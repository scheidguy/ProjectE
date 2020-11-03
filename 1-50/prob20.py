# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:36:23 2020

@author: schei
"""


result = 1
the_sum = 0
for n in range(1, 101):
    result *= n
numstring = str(result)
for digit in numstring:
    the_sum += int(digit)
print(the_sum)
