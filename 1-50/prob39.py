# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:36:08 2020

@author: schei
"""

max_found = 0
the_p = 0
for p in range(1, 1001):
    if p % 100 == 0:
        print(p)
    found = 0
    for a in range(1, round(p/2)):  # can't have a side longer than half perim
        # only check bigger than a to avoid double counting and speed up
        for b in range(a, round(p/2)):
            c = (a**2 + b**2)**0.5
            if a + b + c == p and c.is_integer():
                found += 1
    if found > max_found:
        max_found = found
        the_p = p
print(int(max_found))
print(the_p)
