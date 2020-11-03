# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:16:53 2020

@author: schei
"""


# We know 3/7 = 0.42857142857142855
# We know 428571/1000000 is pretty dang close, so only check in between those
max_val = 1000000
bestN = round(max_val * (3/7))
bestD = max_val
best = bestN / bestD
for d in range(2, max_val):
    if d % 100000 == 0:
        print(d)
    for n in range(int(d*(428571/max_val)), int(d*(3/7) + 1)):
        if n/d > best and n/d < 3/7:
            bestN = n
            bestD = d
            best = n/d
print(f'{bestN} / {bestD} = {best}')
