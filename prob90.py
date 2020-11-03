# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:56:26 2020

@author: schei
"""


from itertools import combinations

comb1 = list(combinations(range(10), 6))
comb2 = comb1
valid = 0
for ind in range(len(comb1)):
    d1 = comb1[ind]
    for d2 in comb2[ind+1:]:
        if not ((0 in d1 and 1 in d2) or (0 in d2 and 1 in d1)):
            continue
        if not ((0 in d1 and 4 in d2) or (0 in d2 and 4 in d1)):
            continue
        if not ((0 in d1 and 9 in d2) or (0 in d2 and 9 in d1)):
            if not ((0 in d1 and 6 in d2) or (0 in d2 and 6 in d1)):
                continue
        if not ((1 in d1 and 6 in d2) or (1 in d2 and 6 in d1)):
            if not ((1 in d1 and 9 in d2) or (1 in d2 and 9 in d1)):
                continue
        if not ((2 in d1 and 5 in d2) or (2 in d2 and 5 in d1)):
            continue
        if not ((3 in d1 and 6 in d2) or (3 in d2 and 6 in d1)):
            if not ((3 in d1 and 9 in d2) or (3 in d2 and 9 in d1)):
                continue
        if not ((4 in d1 and 9 in d2) or (4 in d2 and 9 in d1)):
            if not ((4 in d1 and 6 in d2) or (4 in d2 and 6 in d1)):
                continue
        if not ((6 in d1 and 4 in d2) or (6 in d2 and 4 in d1)):
            if not ((9 in d1 and 4 in d2) or (9 in d2 and 4 in d1)):
                continue
        if not ((8 in d1 and 1 in d2) or (8 in d2 and 1 in d1)):
            continue
        valid += 1
