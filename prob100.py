# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:00:40 2020

@author: schei
"""


import math

# quadratic: b/n * (b-1)/(n-1) = 1/2
# sqrt(2)/2 * sqrt(2)/2 = 1/2
root = (2**0.5) / 2
hits = []
for n in range(round(159140520*5.828427**5), 10**12 + 10**11):
    if n % 10**8 == 0:
        print(n)
    b = math.ceil(root * n)
    if 2*(b*(b-1)) == n*(n-1):
        hits.append([b, n-b, n])
        print(hits[-1])
        break
