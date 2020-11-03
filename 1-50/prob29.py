# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:36:36 2020

@author: schei
"""


nums = []
for a in range(2, 101):
    for b in range(2, 101):
        nums.append(a ** b)
nums = set(nums)
print(len(nums))
