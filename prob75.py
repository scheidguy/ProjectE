# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:03:10 2020

@author: schei
"""


# from math import floor
import time
import numpy as np

start = time.time()
# maxL = 500
# num = 0
# A = []
# B = []
# C = []
# for L in range(12, maxL + 1):
#     found = 0
#     for a in range(3, round(maxL/2)):  # longest side is less than half perim
#         for b in range(a+1, round(maxL/2)):  # don't doubcheck, start at a+1
#             c = (a**2 + b**2)**0.5
#             if c.is_integer() and a+b+c == L:
#                 found += 1
#                 base = True
#                 for i in range(len(A)):
#                     if a % A[i] == 0 and b % B[i] == 0:
#                         base = False
#                         break  # this is just a multiple of a base solution
#                 if base:
#                     A.append(a)
#                     B.append(b)
#                     C.append(int(c))
#                     print(f'{a}^2 + {b}^2 = {int(c)}^2')
#     if found == 1:  # only tabulate if exactly one solution for this L
#         num += 1

# IDEAS #
# Once we've found a 'base' ratio (e.g. 8/15/17), store in arrays A, B, C. Can
#   then determine all future multiples (e.g. 24/45/51) and check those L's.
#   Need to be smarter about examining possible a,b values too. Look for a
#   pattern in the 'base' ratios?


# [112, 1120, 11013] for maxL = [1000, 10000, 100000]
# [332, 678, 1339, 2617, 5274] for maxL = [3000, 6000, 12000, 24000, 48000]
# maxL = 1500000  # this is the actual problem
maxL = 1500000
maxside = round(maxL/2) + 1
# a is smallest side, can't be bigger than 45/45/90 ratio
max_a = int((maxL / (2 + 2**0.5)) + 1)
num = [0 for L in range(maxL+1)]
sq = [(maxL + 1)**2]  # just want index 0 to have an irrelevant value
# store n^2 values to look up quickly later
for n in range(1, maxside):
    sq.append(n**2)
squared = np.array(sq)
for a in range(3, max_a + 1):
    if a % 10000 == 0:
        print(a)
    candidate = squared[a] + squared[a+1:]  # a^2 plus all possible b^2
    overlap = np.intersect1d(candidate, squared)  # see if any integer c^2
    for hyp in overlap:
        c = np.where(hyp == squared)[0][0]
        b = int((c**2 - a**2)**0.5)
        perimeter = a + b + c
        if perimeter <= maxL:
            num[perimeter] += 1
the_sum = 0
for i in range(len(num)):
    if num[i] == 1:
        the_sum += 1
print(f'{the_sum} in {time.time()-start} seconds')
