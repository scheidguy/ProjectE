# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:41:03 2020

@author: schei
"""

amicable = []
d = []
for num in range(0, 10001):
    divsum = 0
    for div in range(1, num):
        if num % div == 0:
            divsum += div
    d.append(divsum)
for num2 in range(2, 10001):
    if num2 == d[num2] or d[num2] > 10000:
        pass
    elif num2 == d[d[num2]]:
        amicable.append(num2)
print(sum(amicable))
