# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:08:52 2020

@author: schei
"""


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


def num_prime_factors(num, primes):
    factors = []
    while num not in primes:
        for prime in primes:
            if num % prime == 0:
                factors.append(prime)
                num /= prime
                break
    if num not in factors:
        factors.append(num)
    return len(set(factors))


primes = calc_primes(1000000)
for num in range(2, 1000000):
    if num % 10000 == 0:
        print(num)
    found_it = True
    for i in range(4):
        if num_prime_factors(num + i, primes) != 4:
            found_it = False
            break
    if found_it:
        print(num)
        break
