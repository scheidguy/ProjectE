# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:16:40 2020

@author: schei
"""


import math

def calc_primes(below_num):
    primes = [2]  # first prime (and only even prime)
    for num in range(3, below_num, 2):  # skip even numbers
        if (num+1) % 1000000 == 0:  # prog report for big prime calculations
            print(f'Found all primes under {num+1}')
        prime_flag = True
        # Only need to check if divisible by other primes
        for prime in primes:
            if num % prime == 0:
                prime_flag = False
                break
            if prime > num ** 0.5:  # only need to check up to the square root
                break
        if prime_flag:
            primes.append(num)
    return primes


primes = calc_primes(10000)
numways = 0
val = 1
while numways < 5:
    numways = 0
    val += 1
    if val in primes: continue
    pr
    for 