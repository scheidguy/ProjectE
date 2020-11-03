# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:16:04 2020

@author: schei
"""


def big_palindrome(max_val):
    palindromes = []
    for num1 in range(100, max_val):
        for num2 in range(num1, max_val):
            result = list(str(num1 * num2))
            if result == result[::-1]:
                palindromes.append(num1 * num2)
    palindromes.sort()
    print(palindromes[-1])
