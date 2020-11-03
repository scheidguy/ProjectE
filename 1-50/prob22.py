# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:05:35 2020

@author: schei
"""


import string

alphabet = string.ascii_uppercase
scores = {}
i = 1
for each in alphabet:
    scores[each] = i
    i += 1
f = open('p022_names.txt', 'r')  # May need to download this again if deleted
string = f.read()
f.close()
names = string.replace('"', '')
names = names.split(',')
names.sort()
the_sum = 0
num = 1
for name in names:
    name_sum = 0
    for letter in name:
        name_sum += scores[letter]
    the_sum += num * name_sum
    num += 1
print(the_sum)
