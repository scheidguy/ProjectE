# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:07:16 2020

@author: schei
"""


size = 1001
the_sum = 1
for n in range(3, size+1, 2):  # build an NxN spiral
    for i in range(4):
        the_sum += (n)**2 - i*(n-1)
print(the_sum)
