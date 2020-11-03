# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:13:54 2020

@author: schei
"""


prev_fibo = 1
curr_fibo = 1
ind = 2
while curr_fibo / 10**999 < 1:
    ind += 1
    next_fibo = prev_fibo + curr_fibo
    prev_fibo = curr_fibo
    curr_fibo = next_fibo
print(ind)
