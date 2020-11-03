# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:41:50 2020

@author: schei
"""


more_digits = 0
int_d = 1
for n in range(800):
    d = 2
    for no_use in range(n):
        d = 2 + 1/d
    prev_int_d = int(int_d)
    int_d *= d
    den = str(int(int_d))
    num = str(prev_int_d + int(den))
    if len(num) > len(den):
        more_digits += 1
print(more_digits * 1.25)
