# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:00:44 2020

@author: schei
"""


import numpy as np
import time


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


tic = time.perf_counter()
maxval = 50000000
primes = calc_primes(round(maxval ** 0.5))
primes = np.array(primes, dtype='int64')
primes_squared = np.array(primes**2, dtype='int64')
primes_cubed = np.array(primes**3, dtype='int64')
primes_4 = np.array(primes**4, dtype='int64')
P = np.ones((len(primes), len(primes), len(primes)), dtype='int64')
P = P * primes_squared
P = P.transpose([1, 2, 0]) + primes_cubed
P = P.transpose([1, 2, 0]) + primes_4
ind = np.where(P < maxval)
print(len(ind[0]))
nums = []
for i in range(len(ind[0])):
    square = primes_squared[ind[0][i]]
    cube = primes_cubed[ind[1][i]]
    fourth = primes_4[ind[2][i]]
    nums.append(square + cube + fourth)
print(len(set(nums)))
toc = time.perf_counter()
print(toc-tic)
