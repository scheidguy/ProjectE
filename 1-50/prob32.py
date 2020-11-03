# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 01:02:20 2020

@author: schei
"""


pandigitals = []
for num1 in range(1, 1000):
    for num2 in range(1, 10000):
        prod = num1 * num2
        numstring = str(prod) + str(num1) + str(num2)
        if len(numstring) == 9:
            if '0' not in numstring:  # zero not allowed
                # must have all 1-9 digits, no duplicates
                if len(set(numstring)) == 9:
                    pandigitals.append(prod)
print(sum(set(pandigitals)))
