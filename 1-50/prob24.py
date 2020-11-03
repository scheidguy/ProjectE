# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:13:54 2020

@author: schei
"""


from itertools import permutations

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = permutations(nums)
perms = list(perms)
print(perms[999999])
