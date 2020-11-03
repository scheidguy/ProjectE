# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:41:33 2020

@author: schei
"""


summa = 0
for i in range(1, 1001):
    summa += i**i
summa = list(str(summa))
print(summa[-10:])
