# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:59:12 2020

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


primes = calc_primes(100000000)
primes.pop(0)  # we know 2 doesn't work for this
primes.pop(1)  # we know 5 doesn't work for this
primes = np.array(primes)
valid = []
for p1 in primes[0:66]:
# for p1 in [3, 7]:
    ind1 = np.where(primes == p1)[0][0] + 1
    # if ind1 % 10 == 0:
    print(ind1)
    for p2 in primes[ind1:66]:
    # for p2 in [7, 11, 17, 19, 37, 73]:
        ind2 = np.where(primes == p2)[0][0] + 1
        # print(p2)
        for p3 in primes[ind2:1228]:
            ind3 = np.where(primes == p3)[0][0] + 1
            the_primes = [str(p1), str(p2), str(p3)]
            all_prime = True
            for i in range(len(the_primes) - 1):
                num_left = len(the_primes) - i - 1
                while num_left > 0:
                    test1 = int(the_primes[i] + the_primes[i+num_left])
                    test2 = int(the_primes[i+num_left] + the_primes[i])
                    num_left -= 1
                    if (test1 not in primes) or (test2 not in primes):
                        all_prime = False
                        break
                if not all_prime:
                    break
            if all_prime:
                valid.append([p1, p2, p3])

# up to primes[166] for 3 digits, primes[1228] for 4 digits
tic = time.perf_counter()
solutions = []
solutions4 = []
for trio in valid:
    p1 = str(trio[0])
    p2 = str(trio[1])
    p3 = str(trio[2])
    print(f'Investigating {trio}')
    maxval = max(trio)
    start4 = np.where(primes == maxval)[0][0] + 1
    for p4 in primes[start4:1228]:  # only care about primes less than 5 digits
        p4 = str(p4)
        if int(p3 + p4) not in primes: continue
        elif int(p4 + p3) not in primes: continue
        elif int(p2 + p4) not in primes: continue
        elif int(p4 + p2) not in primes: continue
        elif int(p1 + p4) not in primes: continue
        elif int(p4 + p1) not in primes: continue
        solutions4.append([p1, p2, p3, p4])
        start5 = np.where(primes == int(p4))[0][0] + 1
        for p5 in primes[start5:1228]:  # only need to check primes > p4
            p5 = str(p5)
            if int(p4 + p5) not in primes: continue
            elif int(p5 + p4) not in primes: continue
            elif int(p3 + p5) not in primes: continue
            elif int(p5 + p3) not in primes: continue
            elif int(p2 + p5) not in primes: continue
            elif int(p5 + p2) not in primes: continue
            elif int(p1 + p5) not in primes: continue
            elif int(p5 + p1) not in primes: continue
            # the_primes = [str(p1), str(p2), str(p3), str(p4), str(p5)]
            # all_prime = True
            # for i in range(len(the_primes) - 1):
            #     num_left = len(the_primes) - i - 1
            #     while num_left > 0:
            #         test1 = int(the_primes[i] + the_primes[i+num_left])
            #         test2 = int(the_primes[i+num_left] + the_primes[i])
            #         num_left -= 1
            #         if (test1 not in primes) or (test2 not in primes):
            #             all_prime = False
            #             break
            #     if not all_prime:
            #         break
            # if all_prime:
            solutions.append([p1, p2, p3, p4, p5])
            print(f'--------- SOLUTION: {[p1, p2, p3, p4, p5]} ---------')
toc = time.perf_counter()
print(toc-tic)
