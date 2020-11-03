# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:51:56 2020

@author: schei
"""


f = open('p079_keylog.txt', 'r')
text = f.read()
f.close()
codes = text.split('\n')
codes.pop()
codes = list(set(codes))  # get rid of duplicates
codes.sort()

for candidate in range(70000000, 100000000):
    c = str(candidate)
    valid = True
    for i in range(10):
        if i == 4 or i == 5:
            continue
        if str(i) not in c:
            valid = False
            break
    if valid:
        for code in codes:
            ind1 = c.index(code[0])
            ind2 = c.index(code[1])
            ind3 = c.index(code[2])
            if ind1 > ind2 or ind1 > ind3 or ind2 > ind3:
                valid = False
                break  # wrong order
        if valid:
            print(candidate)
            break
