# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:20:29 2020

@author: schei
"""


max_sum = 0
for a in range(100):
    for b in range(100):
        num = str(a**b)
        the_sum = 0
        for digit in num:
            the_sum += int(digit)
        if the_sum > max_sum:
            max_sum = the_sum
print(max_sum)
