# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:37:59 2020

@author: schei
"""


# import math

letters = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
hun = 7
thous = 8

# the_sum = 0
# for num in range(1, 1001):
#     if num == 1000:
#         the_sum += thous
#     elif num % 100 == 0:
#         the_sum += hun + letters[int(num/100)]
#     else:
#         extra = 0
#         num_ten = math.floor((num % 100)/10)
#         num_hun = math.floor(num/100)
#         if (num % 100) < 20:
#             extra += letters[num % 100]
#         elif num_ten > 1:
#             extra += tens[num_ten]
#             extra += letters[num % 10]
#         if num_hun >= 1:
#             extra += hun
#             extra += letters[num_hun]
#         the_sum += extra
# the_sum += 3*99*9  # counts all the ands, like in four hundred and forty-two
# print(the_sum)


# alt_sum = 0
# alt_sum += 10*sum(letters)  # trailing digits 1-19
# for j in tens[2:]:
#     alt_sum += 100*j  # tens identifier (e.g. forty) 10 per 100 means 100 tot
# alt_sum += 80*sum(letters[1:9])  # trailing digit in 21-99s
# alt_sum += 900*hun  # 900 numbers with the word hundred in them
# for k in range(1, 10):
#     alt_sum += 100*letters[k]  # letters from number written before hundred
# alt_sum += 3*99*9
# alt_sum += thous + letters[1]
# print(alt_sum)


# FROM BIG TO SMALL
sum3 = 0
sum3 += thous + letters[1]  # one thousand
sum3 += 100*sum(letters[1:10])  # all the numbers before hundred
sum3 += hun*900  # all the hundred words
sum3 += 100*sum(tens[2:])  # all the multiple of ten words, twenty up to ninety
sum3 += 10*sum(letters)  # all the trailing 1-19 digits for each group of 100
sum3 += 80*sum(letters[1:10])  # all the trailing digits 21-99
sum3 += 3*99*9  # Count up all the ands
print(sum3)




















