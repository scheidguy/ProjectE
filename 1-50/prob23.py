# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:37:25 2020

@author: schei
"""


import math
abund = []
for num in range(2, 28124):
    divsum = 1
    # Can't have unknown proper divisor above square root of number
    for div in range(2, math.ceil(num**0.5)):
        if num % div == 0:
            divsum += div  # add the divisor
            divsum += num / div  # add the divisor's partner
    if num % num**0.5 == 0:
        divsum += num**0.5  # add perfect square that was missed in above loop
    if divsum > num:
        abund.append(num)

# construct list of abundant sum pairs that are less than 28124
pairs = []
ind = 0
for a1 in abund:
    for a2 in abund[ind:]:  # only need to check pairs at and above curr num
        if a1 + a2 >= 28124:
            break  # don't need to check for integers above this
        pairs.append(a1 + a2)
        if len(pairs) % 1000000 == 0:
            print(f'{len(pairs)} entries in pairs')
    ind += 1

pairs = set(pairs)  # remove duplicate sums from pairs

# time to sum all numbers less than 28124 that aren't sum of two abunds
the_sum = sum(range(24))  # we know 1-23 aren't because 12 is first abund
for test in range(25, 28124):
    if test not in pairs:
        the_sum += test
print(the_sum)
