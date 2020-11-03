# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:43:51 2020

@author: schei
"""

import math


def get_primes(max_val):
    primes = [2]
    for num in range(3, max_val):
        prime_flag = True
        #Only need to check if divisble by other primes
        for prime in primes:
            if num % prime == 0:
                prime_flag = False
                break

        if prime_flag:
            primes.append(num)

    return primes


def largest_prime_factor(val):
    factors = []
    #the input is prime if can't completely factorize below the sqrt
    max_prime = round(val ** 0.5)
    primes = get_primes(max_prime)
    for num in primes:
        if val % num == 0:
            factors.append(num)
        if math.prod(factors) == val:
            print('got em all, no need to calculate higher primes!')
            break

    print(factors[-1])
