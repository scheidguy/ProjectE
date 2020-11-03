# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:53:33 2020

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


max_val = 510511
primes = calc_primes(max_val)
primes.pop(0)  # we know we don't need to check for 2
biggest = 0
for n in range(510510, max_val, 2):
    coprimes = []
    if n % 1000 == 0:
        print(f'Processing n = {n}')
    for n2 in primes:
        if n2 > n:
            break  # don't need to check primes greater than n, move on
        if n % n2 == 0:
            continue  # evenly divisible so not coprime
        else:  # must be coprime because we know n2 is prime
            coprimes.append(n2)
    for c in coprimes:
        ind = 0
        while c * coprimes[ind] < n:
            if c * coprimes[ind] not in coprimes:  # don't doublecount
                coprimes.append(c * coprimes[ind])
            ind += 1
    phi = 1 + len(coprimes)  # every integer also has 1 as a coprime
    ratio = n / phi
    if ratio > biggest:
        biggest = ratio
        bigN = n
        bigP = phi
        biggest_coprimes = coprimes
print(f'END: {bigN} / {bigP} = {biggest}')
