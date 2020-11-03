# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:41:48 2020

@author: schei
"""


num2find = 5
cubes = [n**3 for n in range(1, 10000)]  # generate a list of cubes
num_digits = [0 for n in range(10)]
prev_length = 0
num_digits = []
for cube in cubes:  # create a list of lists: digit tallies for 0-9
    curr_digits = [0 for n in range(10)]
    for digit in str(cube):
        curr_digits[int(digit)] += 1
    num_digits.append(curr_digits)
for num in num_digits:
    if num_digits.count(num) == num2find:  # count the duplicate tallies
        ind = num_digits.index(num)
        print(cubes[ind])
        break
