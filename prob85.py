# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:25:51 2020

@author: schei
"""


maxdim = 100
target = 2000000
closest = target
for H in range(1, maxdim):
    for W in range(H, maxdim):
        num = 0
        for w in range(1, W + 1):
            for h in range(1, H + 1):
                num += (H - h + 1) * (W - w + 1)
        if abs(target - num) < closest:
            closest = abs(target - num)
            best = [H, W, num]
print(best)
print(best[0] * best[1])
