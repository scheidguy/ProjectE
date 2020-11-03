# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:43:51 2020

@author: schei
"""


def get_sum_primes(below_num):
    primes = [2]
    for num in range(3, below_num, 2):
        prime_flag = True
        # Only need to check if divisible by other primes
        for prime in primes:
            if num % prime == 0:
                prime_flag = False
                break

        if prime_flag:
            primes.append(num)

    return sum(primes)
