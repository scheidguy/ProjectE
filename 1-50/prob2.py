# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:24:43 2020

@author: schei
"""


def sum_fibo(max_val):
    the_sum = 2
    prev_fibo = 1
    curr_fibo = 2
    while curr_fibo < max_val:
        next_fibo = prev_fibo + curr_fibo
        if next_fibo % 2 == 0:
            the_sum += next_fibo

        prev_fibo = curr_fibo
        curr_fibo = next_fibo

    if curr_fibo % 2 == 0:
        the_sum -= curr_fibo

    print(the_sum)
