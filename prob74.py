# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:07:16 2020

@author: schei
"""


from math import factorial
import time

tic = time.perf_counter()
max_val = 1000000
facts = {}
table = {}
num = 0
for d in range(10):
    facts[str(d)] = factorial(d)
for n in range(max_val):
    nstr = str(n)
    cycle = []
    while nstr not in cycle:
        cycle.append(nstr)
        if len(cycle) == 60:
            num += 1
        try:
            result = table[nstr]
        except KeyError:
            newsum = 0
            for digit in nstr:
                newsum += facts[digit]
            result = str(newsum)
            table[nstr] = result
        finally:
            nstr = result
toc = time.perf_counter()
print(f'{num}: Took {toc-tic} seconds')
