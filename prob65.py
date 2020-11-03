# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:45:49 2020

@author: schei
"""


terms = 100
denom = 1
numer = 1
for n in range(terms-1, 1, -1):
    if n % 3 == 0:
        nextdenom = numer
        numer = 2*numer*(n/3) + denom
        denom = nextdenom
    else:
        nextdenom = numer
        numer = denom + numer
        denom = nextdenom
enumer = str(int(2*numer + denom))
edenom = str(int(numer))
the_sum = 0
for digit in enumer:
    the_sum += int(digit)
print(f'{enumer} / {edenom} --> {the_sum}')
