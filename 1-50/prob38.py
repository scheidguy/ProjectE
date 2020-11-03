# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:18:09 2020

@author: schei
"""


pandigitals = []
for num1 in range(1, 100000):
    for num2 in range(2, 10):
        products = ''
        for num3 in range(1, num2 + 1):
            products += str(num1 * num3)
        if len(products) == 9:
            if '0' not in products:  # zero not allowed
                # must have all 1-9 digits, no duplicates
                if len(set(products)) == 9:
                    pandigitals.append(int(products))
print(max(pandigitals))
