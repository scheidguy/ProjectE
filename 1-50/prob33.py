# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:37:25 2020

@author: schei
"""

num_list = []
num_prod = 1
denom_list = []
denom_prod = 1
for numerator in range(11, 100):  # all 2 digit numerators 11-99
    for denominator in range(numerator + 1, 100):  # 2 digit denom
        # skip things like 30/50
        if numerator % 10 != 0 and denominator % 10 != 0:
            num_string = str(numerator)
            denom_string = str(denominator)
            digit1 = num_string[0]
            digit2 = num_string[1]
            if digit1 in denom_string:
                num_string = num_string.replace(digit1, '', 1)
                denom_string = denom_string.replace(digit1, '', 1)
            elif digit2 in denom_string:
                num_string = num_string.replace(digit2, '', 1)
                denom_string = denom_string.replace(digit2, '', 1)
            else:
                continue
            quot1 = numerator / denominator
            quot2 = int(num_string) / int(denom_string)
            if quot1 == quot2:
                num_list.append(numerator)
                denom_list.append(denominator)
                num_prod *= numerator
                denom_prod *= denominator
print(f'{num_prod} / {denom_prod}')
print(num_prod / denom_prod)
