# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:31:16 2020

@author: schei
"""


from itertools import permutations
import time

tic = time.perf_counter()
tris = []
squares = []
pents = []
hexes = []
hepts = []
octs = []
trival = 0
n = 0
while trival < 10000:
    n += 1
    trival = int(1/2 * n * (n + 1))
    if trival in range(1000, 10000):
        tris.append(trival)
    val = n**2
    if val in range(1000, 10000):
        squares.append(val)
    val = int(1/2 * n * (3*n - 1))
    if val in range(1000, 10000):
        pents.append(val)
    val = n * (2*n - 1)
    if val in range(1000, 10000):
        hexes.append(val)
    val = int(1/2 * n * (5*n - 3))
    if val in range(1000, 10000):
        hepts.append(val)
    val = n * (3*n - 2)
    if val in range(1000, 10000):
        octs.append(val)

N = 6
for n8 in octs:
    s8 = str(n8)
    if s8[2] == '0': continue
    print(f'Evaluating Octagonal number: {n8}')
    for n7 in hepts:
        s7 = str(n7)
        if s7[2] == '0': continue
        for n6 in hexes:
            s6 = str(n6)
            if s6[2] == '0': continue
            for n5 in pents:
                s5 = str(n5)
                if s5[2] == '0': continue
                for n4 in squares:
                    s4 = str(n4)
                    if s4[2] == '0': continue
                    for n3 in tris:
                        s3 = str(n3)
                        if s3[2] == '0': continue
                        if s3[2:] not in [s4[0:2], s5[0:2], s6[0:2], s7[0:2], s8[0:2]]: continue
                        if s3[0:2] not in [s4[2:], s5[2:], s6[2:], s7[2:], s8[2:]]: continue
                        if s4[2:] not in [s3[0:2], s5[0:2], s6[0:2], s7[0:2], s8[0:2]]: continue
                        if s4[0:2] not in [s3[2:], s5[2:], s6[2:], s7[2:], s8[2:]]: continue
                        if s5[2:] not in [s3[0:2], s4[0:2], s6[0:2], s7[0:2], s8[0:2]]: continue
                        if s5[0:2] not in [s3[2:], s4[2:], s6[2:], s7[2:], s8[2:]]: continue
                        if s6[2:] not in [s3[0:2], s4[0:2], s5[0:2], s7[0:2], s8[0:2]]: continue
                        if s6[0:2] not in [s3[2:], s4[2:], s5[2:], s7[2:], s8[2:]]: continue
                        if s7[2:] not in [s3[0:2], s4[0:2], s5[0:2], s6[0:2], s8[0:2]]: continue
                        if s7[0:2] not in [s3[2:], s4[2:], s5[2:], s6[2:], s8[2:]]: continue
                        the_set = [n3, n4, n5, n6, n7, n8]
                        if len(set(the_set)) != N:
                            continue  # duplicate values no bueno
                        the_set.sort()
                        perm = permutations(the_set)
                        for p in list(perm):
                            if p[0] != the_set[0]:
                                break  # since circular, can skip rest of perms
                            for i in range(N):
                                if i == N - 1:
                                    if str(p[i])[2:] == str(p[0])[0:2]:
                                        print(p)
                                        print(sum(the_set))
                                        break
                                elif str(p[i])[2:] != str(p[i+1])[0:2]:
                                    break
toc = time.perf_counter()
print(toc-tic)
