# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:08:27 2020

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


def get_prime_factorization(num, primes):
    factored = []
    factor = num
    for prime in primes:
        first = True
        while factor % prime == 0:
            factor /= prime
            if first:  # don't need to add if already did
                first = False
                factored.append(prime)
        if factor in primes:
            factored.append(factor)
            break  # we have the complete prime factorization
        if factor == 1:
            break  # we have the complete prime factorization
    return factored


tic = time.perf_counter()
max_val = 1000001
primes = calc_primes(max_val)
parr = np.array(primes.copy())
N = []
num = 0
for d in range(2, max_val):
    N.append(d-1)
    if d % 10000 == 0:
        print(d)
    if d in parr:  # can't reduce fraction with this denominator
        num += d - 1  # count all n/d except n == d (because then n/d = 1)
    elif d**0.5 in parr:  # denominator is a perfect square of a prime
        num += d - d**0.5  # e.g. n/25 we only count all but n=[5,10,15,20]
    else:  # denominator is a composite number and not perfect square
        factored = get_prime_factorization(d, parr)
        numerators = np.array(N)
        for factor in factored:
            ind = np.where(numerators % factor == 0)[0]
            if ind.size > 0:
                numerators = np.delete(numerators, ind)
        num += len(numerators)
print(num)
toc = time.perf_counter()
print(toc-tic)
