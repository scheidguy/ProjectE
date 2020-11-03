# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:14:01 2020

@author: schei
"""


def get_sum_3_and_5(max_val):
    the_sum = 0
    for num in range(1, max_val):
        if num % 3 == 0 or num % 5 == 0:
            the_sum += num

    print(the_sum)
