# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:41:53 2020

@author: schei
"""


import math

with open('p099_base_exp.txt', 'r') as f:
    text = f.readlines()

biggest = 0
num = 0
for line in text:
    num += 1
    pair = line.split(',')
    base = int(pair[0])
    exp = int(pair[1])
    power2 = math.log2(base) * exp
    if power2 > biggest:
        biggest = power2
        bignum = num
print(bignum)
