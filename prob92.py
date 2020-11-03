# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:07:32 2020

@author: schei
"""


import time

tic = time.perf_counter()
maxval = 10000000
num = 0
for n in range(1, maxval):
    if n % 1000000 == 0:
        print(n)
    nstr = str(n)
    while nstr not in ['1', '89']:
        chain = 0
        for digit in nstr:
            chain += int(digit) ** 2
        nstr = str(chain)
    if nstr == '89':
        num += 1
print(num)
toc = time.perf_counter()
print(toc-tic)
