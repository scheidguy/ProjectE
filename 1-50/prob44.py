# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:40:07 2020

@author: schei
"""


def calc_pents(max_val):
    pents = []
    for n in range(1, max_val+1):
        pents.append(int(0.5 * n * (3*n - 1)))
    return pents


pents = calc_pents(5000)
diffs = []
for p1 in pents:
    start = pents.index(p1)
    if start % 10 == 0:
        print(start)
    for p2 in pents[start+1:]:
        if p1 + p2 in pents and p2 - p1 in pents:
            diffs.append(p2 - p1)
print(min(diffs))
