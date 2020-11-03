# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:14:49 2020

@author: schei
"""


import time
from decimal import *

getcontext().prec = 75
tic = time.perf_counter()
maxval = 10**9
perims = 0
almost = []
for iso in range(2, round(maxval/3) + 1):
    if iso % 10**7 == 0:
        print(iso)
    iso = Decimal(iso)
    h = Decimal(iso*iso - ((iso-1)/2)*((iso-1)/2)).sqrt()
    if ((iso-1) * h / 2) % 1 == 0:
        perims += int(iso)*3 - 1
        almost.append(int(iso))
    h = Decimal(iso*iso - ((iso+1)/2)*((iso+1)/2)).sqrt()
    if ((iso+1) * h / 2) % 1 == 0:
        perims += int(iso)*3 + 1
        almost.append(int(iso))
print(perims)
toc = time.perf_counter()
print(toc-tic)
