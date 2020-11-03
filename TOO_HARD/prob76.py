# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:35:31 2020

@author: schei
"""


import time
import math

tic = time.perf_counter()
# val = 16
# store values for # of paths, initialize with 1+1 = 2
# 1+2=3 and 1+1+1=3
# 1+1+1+1=4 and 1+1+2=4 and 1+3=4 and 2+2=4
# table = [0, 0, 1, 2, 4, 6, 10, 14, 21, 29, 41, 55, 76, 100, 134, 175]
# valid = []
# for one in range(0, val):
#     for two in range(0, val, 2):
#         for three in range(0, val, 3):
#             for four in range(0, val, 4):
#                 for five in range(0, val, 5):
#                     for six in range(0, val, 6):
#                         for seven in range(0, val, 7):
#                             for eight in range(0, val, 8):
#                                 for nine in range(0, val, 9):
#                                     for ten in range(0, val, 10):
#                                         for el in range(0, val, 11):
#                                             for tw in range(0, val, 12):
#                                                 for th in range(0, val, 13):
#                                                     for fo in range(0, val, 14):
#                                                         the_sum = one+two+three+four+five+six+seven+eight+nine+ten+el+tw+th+fo
#                                                         if the_sum == val-1:
#                                                             templist = [one,two,three,four,five,six,seven,eight,nine,ten,el,tw,th,fo]
#                                                             if templist not in valid:
#                                                                 valid.append(templist)

val = 2
max_val = 10
table = [0, 0]
while val <= max_val:
    num = 0
    n = 1
    while n <= val:
        for i in range(1, math.floor(val/n) + 1):
            remainder = val % n
            if remainder:
                num += table[remainder] + 1
            else:
                num += 1
        n += 1
    table.append(num)
    val += 1
print(table)
