# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:10:24 2020

@author: schei
"""


from decimal import *

getcontext().prec = 125
the_sum = 0
for n in range(100):
    if n in [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
        continue
    root = str(Decimal(n).sqrt())
    root = root.replace('.', '')
    for digit in root[0:100]:
        the_sum += int(digit)
print(the_sum)
