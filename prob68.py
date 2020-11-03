# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:52:03 2020

@author: schei
"""


from itertools import permutations

# gon = [[], [], []]
# valid = []
# for n in range(1, 7):
#     nums = [1, 2, 3, 4, 5, 6]
#     nums.remove(n)
#     not_done = True
#     while not_done:
#         if len(nums) == 0:  # haven't removed all the options yet
#             not_done = False

gon = permutations(range(1, 11))
valid = []
for i in gon:
    if i[1] == 10 or i[2] == 10 or i[4] == 10 or i[6] == 10 or i[8] == 10:
        continue  # this means 10 isn't on the outside of the 5gon, 17 digits
    outside = []
    if sum(i[0:3]) == sum(i[2:5]):  # check that we are "magic"
        if sum(i[0:3]) == sum(i[4:7]):
            if sum(i[0:3]) == sum(i[6:9]):
                if sum(i[0:3]) == (sum(i[8:]) + i[1]):
                    outside.append(i[0])
                    outside.append(i[3])
                    outside.append(i[5])
                    outside.append(i[7])
                    outside.append(i[9])
                    ind = i.index(min(outside))
                    s = []
                    for index in range(len(i)):
                        s.append(str(i[index]))
                    if ind == 0:
                        S = s[0]+s[1]+s[2]+s[3]+s[2]+s[4]+s[5]+s[4]+s[6]+s[7]+s[6]+s[8]+s[9]+s[8]+s[1]
                        valid.append(int(S))
                    elif ind == 3:
                        S = s[3]+s[2]+s[4]+s[5]+s[4]+s[6]+s[7]+s[6]+s[8]+s[9]+s[8]+s[1]+s[0]+s[1]+s[2]
                        valid.append(int(S))
                    elif ind == 5:
                        S = s[5]+s[4]+s[6]+s[7]+s[6]+s[8]+s[9]+s[8]+s[1]+s[0]+s[1]+s[2]+s[3]+s[2]+s[4]
                        valid.append(int(S))
                    elif ind == 7:
                        S = s[7]+s[6]+s[8]+s[9]+s[8]+s[1]+s[0]+s[1]+s[2]+s[3]+s[2]+s[4]+s[5]+s[4]+s[6]
                        valid.append(int(S))
                    elif ind == 9:
                        S = s[9]+s[8]+s[1]+s[0]+s[1]+s[2]+s[3]+s[2]+s[4]+s[5]+s[4]+s[6]+s[7]+s[6]+s[8]
                        valid.append(int(S))
print(max(valid))
