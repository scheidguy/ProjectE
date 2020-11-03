# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:53:57 2020

@author: schei
"""


def get_primes(below_num):
    primes = [2]  # first prime (and only even prime)
    for num in range(3, below_num, 2):  # skip even numbers
        if (num+1) % 100000 == 0:  # progress report for big prime calculations
            print(f'Found all primes under {num+1}')
        prime_flag = True
        # Only need to check if divisible by other primes
        for prime in primes:
            if num % prime == 0:
                prime_flag = False
                break

        if prime_flag:
            primes.append(num)

    return primes


primes = get_primes(1000000)
trunc = []
for prime in primes:
    if prime < 10:
        continue  # 1 digit primes don't count as truncatable
    n = str(prime)
    truncatable_L = True
    while truncatable_L:
        n = n[1:]
        if int(n) not in primes:
            truncatable_L = False
        elif len(n) == 1:
            break  # down to a 1 digit number, need to exit while loop
    m = str(prime)
    truncatable_R = True
    while truncatable_R:
        m = m[0:-1]
        if int(m) not in primes:
            truncatable_R = False
        elif len(m) == 1:
            break  # down to a 1 digit number, need to exit while loop
    if truncatable_L and truncatable_R:
        trunc.append(prime)
print(sum(trunc))
