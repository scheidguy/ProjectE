# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:56:18 2020

@author: schei
"""


not_done = True
num = 0
while not_done:
    num += 1
    for mult in [6, 5, 4, 3, 2]:
        s1 = str(num)
        s2 = str(num * mult)
        for digit in s1:
            s2 = s2.replace(digit, '')
        if len(s2) != 0:
            break
        if mult == 2:
            not_done = False
            print(num)
