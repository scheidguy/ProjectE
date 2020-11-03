# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:08:25 2020

@author: schei
"""

from itertools import permutations

perm = permutations(range(10))
perm = list(perm)
divs = [2, 3, 5, 7, 11, 13, 17]
special = []
for pan in perm:
    all_good = True
    p = ''
    for digit in range(10):
        p += str(pan[digit])
    for i in range(1, 8):
        num = int(p[i] + p[i+1] + p[i+2])
        if num % divs[i-1] != 0:
            all_good = False
            break
    if all_good:
        special.append(int(p))
print(sum(special))
