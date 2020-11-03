# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:07:16 2020

@author: schei
"""


f = open('p059_cipher.txt', 'r')
text = f.read()
f.close()
crypts = text.split(',')


words = [' the ', ' and ']  # common words to look for, could add ['of', 'to']
ascii_dict = {i: chr(i) for i in range(128)}  # create ascii code dictionary
lowercase_begin = 97
lowercase_end = 123

found_it = False
for key1 in range(lowercase_begin, lowercase_end):
    print(key1)
    for key2 in range(lowercase_begin, lowercase_end):
        for key3 in range(lowercase_begin, lowercase_end):
            ind = 0
            decrypted = ''
            the_sum = 0
            for char in crypts:
                if ind % 3 == 0:
                    decrypted += ascii_dict[key1 ^ int(char)]
                    the_sum += key1 ^ int(char)
                elif ind % 3 == 1:
                    decrypted += ascii_dict[key2 ^ int(char)]
                    the_sum += key2 ^ int(char)
                elif ind % 3 == 2:
                    decrypted += ascii_dict[key3 ^ int(char)]
                    the_sum += key3 ^ int(char)
                ind += 1
            for i in range(len(words)):
                if decrypted.find(words[i]) == -1:
                    break
                elif i == len(words) - 1:  # reached end of list and found all
                    found_it = True
            if found_it:
                break
        if found_it:
            break
    if found_it:
        break
print(decrypted)
print(the_sum)
