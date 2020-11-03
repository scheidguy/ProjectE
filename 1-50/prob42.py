# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:49:07 2020

@author: schei
"""


import string


def calc_triangle_nums(max_val):
    tri = []
    for n in range(1, max_val + 1):
        tri.append(0.5 * n * (n + 1))
    return tri


alphabet = string.ascii_uppercase

f = open('p042_words.txt', 'r')
text = f.read()
f.close()
text = text.replace('"', '')
words = text.split(',')

tri = calc_triangle_nums(1000)
num = 0
for word in words:
    score = 0
    for letter in word:
        score += alphabet.find(letter) + 1
    if score in tri:
        num += 1
print(num)
