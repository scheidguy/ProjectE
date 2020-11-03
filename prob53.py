# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:37:45 2020

@author: schei
"""


def n_choose_r(n, r):
    import math
    numerator = math.factorial(n)
    denominator = math.factorial(r) * math.factorial(n-r)
    return int(numerator / denominator)


counter = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if n_choose_r(n, r) > 1000000:
            counter += 1
print(counter)
