# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:40:09 2020

@author: schei
"""


with open('p098_words.txt', 'r') as f:
    text = f.read().replace('"', '').split(',')

words = [[] for i in range(15)]
anagrams = [[] for i in range(15)]
for word in text:
    words[len(word)].append(word)

for length in range(len(words)):
    w = words[length]
    for ind1 in range(len(w)):
        for ind2 in range(ind1 + 1, len(w)):
            if sorted(w[ind1]) == sorted(w[ind2]):
                anagrams[length].append([w[ind1], w[ind2]])

squares9 = [str(n**2) for n in range(10**4, 31623)]
bigs = []
for square in squares9:
    if len(set(square)) == 9:
        bigs.append(square)
for b in bigs:
    word1 = anagrams[9][0][0]
    word2 = anagrams[9][0][1]
    digits = list(b)
    for i in range(len(word1)):
        word2 = word2.replace(word1[i], digits[i])
    if word2 in bigs:
        print(word1)
        print(word2)

squares8 = [str(n**2) for n in range(3163, 10**4)]
bigs = []
for square in squares8:
    if len(set(square)) == 8:
        bigs.append(square)
for b in bigs:
    word1 = anagrams[8][0][0]
    word2 = anagrams[8][0][1]
    digits = list(b)
    for i in range(len(word1)):
        word2 = word2.replace(word1[i], digits[i])
    if word2 in bigs:
        print(word1)
        print(word2)

squares6 = [str(n**2) for n in range(317, 10**3)]
bigs = []
for square in squares6:
    if len(set(square)) == 6:
        bigs.append(square)
for ind in [1, 2, 3, 6]:
    for b in bigs:
        word1 = anagrams[6][ind][0]
        word2 = anagrams[6][ind][1]
        digits = list(b)
        for i in range(len(word1)):
            word2 = word2.replace(word1[i], digits[i])
        if word2 in bigs:
            print(word1)
            print(word2)
squares6_list = [list(s) for s in squares6]
for pattern in squares6_list:
    newpattern = pattern[2:]
    newpattern.append(pattern[1])
    newpattern.append(pattern[0])
    if newpattern in squares6_list and pattern[0] == pattern[4]:
        # print(newpattern)
        print(pattern)
    newpattern = pattern[2:]
    newpattern.append(pattern[0])
    newpattern.append(pattern[1])
    if newpattern in squares6_list and pattern[1] == pattern[3]:
        # print(newpattern)
        print(pattern)
    newpattern = pattern[0:2]
    newpattern.extend([pattern[4], pattern[3], pattern[2], pattern[5]])
    if newpattern in squares6_list and pattern[0] == pattern[3]:
        if len(set(pattern)) == 5:
            print(newpattern)
            print(pattern)
            print('')

squares5 = [str(n**2) for n in range(10**2, 317)]
bigs = []
for square in squares5:
    if len(set(square)) == 5:
        bigs.append(square)
for ind in range(len(anagrams[5])):
    for b in bigs:
        word1 = anagrams[5][ind][0]
        word2 = anagrams[5][ind][1]
        digits = list(b)
        for i in range(len(word1)):
            word2 = word2.replace(word1[i], digits[i])
        if word2 in bigs:
            print(word1)
            print(word2)
            print(digits)
