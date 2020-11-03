# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:47:29 2020

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


primes = calc_primes(10000)
found_it = False
for prime in primes:
    if prime > 1000 and prime != 1487:
        for num in range(1, 4500):
            num2 = prime + num
            num3 = prime + 2*num
            if num3 >= 10000:
                break  # we know they are 4 digit numbers
            if num2 in primes and num3 in primes:
                s1 = str(prime)
                s2 = str(num2)
                s3 = str(num3)
                found_it = True
                for digit in s1:
                    if digit not in s2 or digit not in s3:
                        found_it = False
                        break
                    else:
                        s2 = s2.replace(digit, '', 1)
                        s3.replace(digit, '', 1)
                if found_it:
                    break
    if found_it:
        print(s1 + str(num2) + str(num3))
        break
