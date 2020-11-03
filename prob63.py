# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:17:02 2020

@author: schei
"""


hits = [1]
for n in range(2, 10):
    exp = 0
    not_done = True
    while not_done:
        exp += 1
        val = n ** exp
        if len(str(val)) == exp:
            hits.append(val)
        elif len(str(val)) < exp:
            not_done = False
print(len(hits))
