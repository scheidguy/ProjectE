# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:46:33 2020

@author: schei
"""

the_sum = 0
for num in range(1000000):
    dec_string = str(num)
    if dec_string == dec_string[::-1]:
        bin_string = bin(num)
        bin_string = bin_string[2:]
        if bin_string == bin_string[::-1]:
            the_sum += num
print(the_sum)
