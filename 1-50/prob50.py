# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:20:31 2020

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


primes = calc_primes(1000000)
longest = 0
the_prime = 0
inc = 0
for prime in primes:
    inc += 1
    if inc % 1000 == 0:
        print(inc)
    for p1 in primes:
        if p1 > prime/50000:
            break
        ind = primes.index(p1)
        test = []
        length = 0
        while sum(test) < prime:
            test.append(primes[ind])
            ind += 1
            length += 1
            if sum(test) == prime and length > longest:
                longest = length
                the_prime = prime
print(the_prime)