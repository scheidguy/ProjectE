# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:45:46 2020

@author: schei
"""


def get_primes(below_num):
    primes = [2]  # first prime (and only even prime)
    for num in range(3, below_num, 2):  # skip even numbers
        prime_flag = True
        # Only need to check if divisible by other primes
        for prime in primes:
            if num % prime == 0:
                prime_flag = False
                break

        if prime_flag:
            primes.append(num)

    return primes


# check equations of the form n**2 + a*n + b where a < 1000 and b <= 1000
primes = get_primes(10000)
numprimes = 0
A = 0
B = 0
for a in range(-1000, 1000):
    if a % 100 == 0:
        print(f'a = {a}')
    for b in range(-1000, 1001):
        woohoo = True
        for numb in range(0, abs(a) + 1):
            val = numb**2 + a*numb + b
            if val not in primes:
                woohoo = False
                break
        if woohoo and numprimes < numb:
            numprimes = numb
            A = a
            B = b
print(f'{A*B}')


# CHECKED THE BELOW FIRST TO SEE IF WE COULD DO BETTER WITH OTHER FORM

# for b in range(-1000, 1001):
#     woohoo = True
#     for numb in range(0, abs(b) - 1):
#         val = numb**2 + numb + b
#         if val not in primes:
#             woohoo = False
#             break
#     if woohoo:
#         numprimes = numb
#         A = 1
#         B = b
