# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:40:05 2020

@author: schei
"""


nums = []
for n in range(10, 10000000):  # ignore single digit numbers
    num = str(n)
    sums = 0
    for digit in num:
        sums += int(digit) ** 5
    if sums == n:
        nums.append(n)
print(sum(nums))
