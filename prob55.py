# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:51:25 2020

@author: schei
"""


counter = 0
for num in range(1, 10001):
    n = str(num)
    lychrel = True
    for i in range(50):
        test = int(n) + int(n[::-1])
        n = str(test)
        if n == n[::-1]:
            lychrel = False
            break
    if lychrel:
        counter += 1
print(counter)
