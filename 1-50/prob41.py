# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:21:05 2020

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


primes = calc_primes(10000000)
pandigitals = []
for prime in primes:
    st = str(prime)
    found = True
    for digit in range(1, len(st) + 1):
        if str(digit) not in st:
            found = False
            break
    if found:
        pandigitals.append(prime)
print(max(pandigitals))
