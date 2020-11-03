# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:53:51 2020

@author: schei
"""


max_val = 20
num = 20
not_done = True
while not_done:
    for mod in range(max_val, 1, -1):
        if num % mod != 0:
            num += 1
            break
        elif mod == 2:
            not_done = False
            print(num)
            break
