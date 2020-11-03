# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:37:29 2020

@author: schei
"""

### RESEARCH PELL'S EQUATION (problem 94 forum) or vikt (100 forum) ###

import numpy as np
import time

tic = time.perf_counter()
ysquares = np.arange(1, 10**9, dtype='int64') ** 2

largestX = 0
for D in range(1, 100):
    if D % 10 == 0:
        print(f'Processing D = {D}')
    if (D**0.5).is_integer():
        continue  # problem statement says we can disregard squares

    x = (1 + D*ysquares) ** 0.5
    first = np.where(x % 1 == 0)[0][0]
    x = x[first]
    y = ((x**2 - 1) / D) ** 0.5
    if x > largestX:
        largestX = x
        largestY = y
        BigD = D
        print(f'{int(x)}^2 - {D}*{int(y)}^2 = 1')


    # keep_looking = True
    # # x = 1
    # y = 0
    # while keep_looking:
    #     y += 1
    #     x = (1 + D*y**2) ** 0.5
    #     int_x = round(x)
    #     if int_x**2 - D*y**2 == 1:
    #         if int_x > largestX:
    #             largestX = int_x
    #             largestY = y
    #             BigD = D
    #             print(f'{int_x}^2 - {D}*{y}^2 = 1')
    #         keep_looking = False
    #         break  # move to next x after finding minimal solution


        # x += 1
        # y = ((x**2 - 1) / D) ** 0.5
        # int_y = round(y)
        # if x**2 - D*int_y**2 == 1:
        #     if x > largestX:
        #         largestX = x
        #         largestY = int_y
        #         BigD = D
        #     keep_looking = False
        #     break  # move to next x after finding minimal solution
        # if y > 226153980:  # we know this was the D=61 solution
        #     print(f'(x,y,D) = {x}, {y}, {D}')
        #     break
print(f'ALL DONE: {largestX}^2 - {BigD}*{largestY}^2 = 1 ---> D = {BigD}')
toc = time.perf_counter()
print(toc-tic)
