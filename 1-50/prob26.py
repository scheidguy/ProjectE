# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:24:43 2020

@author: schei
"""


# THIS SOLUTION SUX, I MANUALLY INSPECTED THE BIGGEST NUMS AND IT IS 983
from decimal import *

getcontext().prec = 10000

numlist = []
lenlist = []

den = 1
longest = 6  # has to be better than 1/7 = 0.142857142857
num = 7  # 1/7 is the num to beat
while den < 999:
    den += 1
    frac = str(Decimal(den) ** -1)
    ind = 2  # first digit after decimal
    while frac[ind] == 0:
        ind += 1  # this finds index of first nonzero digit after decimal
        # skip over things like 0.1666 and 0.443443443
    if frac[ind:ind+3] == frac[ind+3:ind+6]:
        continue
    if frac[ind+1:ind+4] == frac[ind+4:ind+7]:
        continue
    if frac[ind:ind+4] == frac[ind+4:ind+8]:
        continue
    if frac[ind+1:ind+5] == frac[ind+5:ind+9]:
        continue
    if frac[ind:ind+5] == frac[ind+5:ind+10]:
        continue
    if frac[ind+1:ind+6] == frac[ind+6:ind+11]:
        continue
    # check for larger repeating
    for inc in range(495, 2000):
        if frac[ind:ind+inc] == frac[ind+inc:ind+2*inc]:
            longest = inc
            num = den
            numlist.append(num)
            lenlist.append(inc)
            #break

print(f'{longest} repeating digits: 1/{num} = {1/num}')

newnum = 0
ind = -1
unique_nums = []
unique_lengths = []
for i in numlist:
    ind += 1
    if i == newnum:
        continue
    else:
        newnum = i
        unique_nums.append(i)
        unique_lengths.append(lenlist[ind])
        
