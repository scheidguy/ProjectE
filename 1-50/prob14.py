# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:42:48 2020

@author: schei
"""

longest = 0
longest_num = 0
for num in range(1, 1000001):
    seq = num
    length = 1
    while seq != 1:
        if seq % 2 == 0:
            seq /= 2
        else:
            seq = 3*seq + 1
        length += 1
    if length > longest:
        longest = length
        longest_num = num
    if num % 100000 == 0:
        print('processed 100k')

print(f'{longest_num}: {longest} steps')
