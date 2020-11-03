# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:20:19 2020

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


max_val = 1000000
primes = get_primes(max_val)
circ = 0
for num in primes:
    n = str(num)
    circular = True
    for digit in range(1, len(n)):
        rotated = n[digit:] + n[0:digit]
        if int(rotated) not in primes:
            circular = False
            break
    if circular:
        circ += 1
print(circ)
