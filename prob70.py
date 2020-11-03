# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:23:56 2020

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


# assume there is a permutation of the product of 2 primes, and
#   we just need to find the one with the smallest ratio. Primes have the
#   smallest ratios N/(N+1) but will never be permuations. Product of two
#   primes is the next best thing.
MAX = 10**7
max_val = 10**4  # only need to examine primes around sqrt(10^7)
primes = calc_primes(max_val)
smallest = 999
the_n = 0
for p1 in primes:
    for p2 in primes:
        if p1 * p2 > MAX:
            break  # every successive p2 will be too big for this p1
        n = p1 * p2
        nstr = str(n)
        phi = n - p1 - p2 + 1
        pstr = str(phi)
        ind = 0
        perm = True
        while len(pstr) > 0:
            prev_len = len(pstr)
            pstr = pstr.replace(nstr[ind], '', 1)
            if prev_len != len(pstr) + 1:
                perm = False
                break
            ind += 1
        if perm:
            ratio = n / phi
            if ratio < smallest:
                smallest = ratio
                the_n = n
print(f'phi({the_n}) --> {smallest}')
