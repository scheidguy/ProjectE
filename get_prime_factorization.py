# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:41:11 2020

@author: schei
"""


# Can pass in np.array(primes) to speed things up if needed
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
