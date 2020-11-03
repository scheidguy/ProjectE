# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:05:45 2020

@author: schei
"""


import numpy as np
import time

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


tic = time.perf_counter()
size = 8
primes = calc_primes(1000000)
primes = np.array(primes)
all_done = False
processed = 0
for prime in primes:
    processed += 1
    if processed % 1000 == 0:
        print(f'Processed first {processed} primes')
    if size >= 7 and prime < 100:
        continue
    p = str(prime)

    # for d1 in range(len(p)):  # try changing just one digit
    #     count = 0
    #     family = []
    #     for replace in '0123456789':
    #         if d1 == 0 and replace == '0':  # no leading zeros
    #             count += 1
    #             continue
    #         if d1 == len(p) - 1:  # last digit
    #             new = p[0:d1] + replace
    #         else:
    #             new = p[0:d1] + replace + p[d1+1:]
    #         if int(new) not in primes:
    #             count += 1
    #         else:
    #             family.append(int(new))
    #     if count <= 10-size:
    #         print(family)
    #         all_done = True
    #         break

    # for d1 in range(len(p) - 1):  # try changing 2 digits
    #     for d2 in range(d1 + 1, len(p)):
    #         count = 0
    #         family = []
    #         for replace in '0123456789':
    #             if d1 == 0 and replace == '0':  # no leading zeros
    #                 count += 1
    #                 continue
    #             if d2 == len(p) - 1:
    #                 new = p[0:d1] + replace + p[d1+1:d2] + replace
    #             else:
    #                 new = p[0:d1] + replace + p[d1+1:d2] + replace + p[d2+1:]
    #             if int(new) not in primes:
    #                 count += 1
    #             else:
    #                 family.append(int(new))
    #             if count > 10-size:
    #                 break
    #         if count <= 10-size:
    #             print(family)
    #             all_done = True
    #             break
    #     if all_done:
    #         break

    for d1 in range(len(p) - 2):  # try changing 3 digits
        for d2 in range(d1 + 1, len(p) - 1):
            for d3 in range(d2 + 1, len(p)):
                count = 0
                family = []
                for replace in '0123456789':
                    if d1 == 0 and replace == '0':  # no leading zeros
                        count += 1
                        continue
                    if d3 == len(p) - 1:
                        new = p[0:d1] + replace + p[d1+1:d2] + replace + p[d2+1:d3] + replace
                    else:
                        new = p[0:d1] + replace + p[d1+1:d2] + replace + p[d2+1:d3] + replace + p[d3+1:]
                    if int(new) not in primes:
                        count += 1
                    else:
                        family.append(int(new))
                    if count > 10-size:
                        break
                if count <= 10-size:
                    print(family)
                    all_done = True
                    break
            if all_done:
                break
        if all_done:
            break

    if all_done:
        break
toc = time.perf_counter()
print(toc-tic)
