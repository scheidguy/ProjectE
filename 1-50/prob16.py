# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:28:30 2020

@author: schei
"""


num = str(2 ** 1000)
the_sum = 0
for digit in num:
    the_sum += int(digit)
print(the_sum)
