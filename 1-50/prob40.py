# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:02:02 2020

@author: schei
"""

champ = ''
prod = 1
not_done = True
digit = 0
flags = [True, True, True, True, True]
while not_done:
    digit += 1
    champ += str(digit)
    if len(champ) == 1:
        prod *= int(champ[0])
    if len(champ) >= 10 and flags[0]:
        flags[0] = False
        prod *= int(champ[9])
    if len(champ) >= 100 and flags[1]:
        flags[1] = False
        prod *= int(champ[99])
    if len(champ) >= 1000 and flags[2]:
        flags[2] = False
        prod *= int(champ[999])
    if len(champ) >= 10000 and flags[3]:
        flags[3] = False
        prod *= int(champ[9999])
    if len(champ) >= 100000 and flags[4]:
        flags[4] = False
        prod *= int(champ[99999])
    if len(champ) >= 1000000:
        prod *= int(champ[999999])
        not_done = False
print(prod)
