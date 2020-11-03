# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:29:39 2020

@author: schei
"""

a = 0
b = 0
c = 0
done_flag = False
max_val = 1000
for a in range(1, max_val):
    a += 1
    for b in range(1, max_val):
        b += 1
        c = (a**2 + b**2) ** 0.5
        if a+b+c == 1000:
            done_flag = True
            break
    if done_flag:
        break

print(a*b*c)
