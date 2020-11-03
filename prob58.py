# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:43:17 2020

@author: schei
"""


def calc_primes(below_num):
    primes = [2]  # first prime (and only even prime)
    for num in range(3, below_num, 2):  # skip even numbers
        if (num+1) % 10000000 == 0:  # prog report for big prime calculations
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


primes = calc_primes(1000000)
not_done = True
dim = 1
corner = 1
diag_primes = 0
thresh = 0.1
while not_done:
    dim += 2
    if (dim-1) % 100000 == 0:
        print(f'Calculating {dim} by {dim}')
    for position in range(4):
        corner = corner + dim - 1
        if position == 3:  # lower right is always a perfect square
            continue
        elif corner in primes:
            diag_primes += 1
        elif corner > primes[-1]:
            if corner ** 0.5 > primes[-1]:
                not_done = False
                print('NEED A BIGGER ARRAY OF PRIMES')
            else:
                for prime in primes:
                    if corner % prime == 0:
                        break
                    if prime > corner ** 0.5:  # only check up to the sqrt
                        diag_primes += 1
                        break

    ratio = diag_primes / (2*dim - 1)
    if ratio < thresh:
        not_done = False
        print(f'{dim}x{dim}: {ratio}')
