# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:10:34 2020

@author: schei
"""

num = 5983
tri = 17901136
num_divisors = 0
while num_divisors <= 500:
    num_divisors = 2
    num += 1
    tri += num
    # no point in for looping unless divisibe by most common numbers
    if tri % 10 == 0 and tri % 3 == 0:
        for i in range(2, tri):
            if tri % i == 0:
                num_divisors += 1
print(f'{num}, {tri}')
