# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 01:34:34 2020

@author: schei
"""

import math

curios = []
for num in range(3, 2000000):  # skipping 1 and 2 per the problem statement
    sums = 0
    for digit in str(num):
        sums += math.factorial(int(digit))
    if sums == num:
        curios.append(num)
print(sum(curios))
