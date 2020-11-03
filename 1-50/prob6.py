# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:39:22 2020

@author: schei
"""


def sumsquare_diff(max_val):
    the_sum = 0
    for num in range(1, max_val + 1):
        the_sum += num ** 2

    the_square = sum(range(1, max_val + 1)) ** 2
    return the_square - the_sum
