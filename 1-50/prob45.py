# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:21:06 2020

@author: schei
"""


def calc_pents(max_val):
    pents = []
    for n in range(1, max_val+1):
        pents.append(int(0.5 * n * (3*n - 1)))
    return pents


def calc_hexes(max_val):
    hexes = []
    for n in range(1, max_val+1):
        hexes.append(n * (2*n - 1))
    return hexes


def calc_tris(max_val):
    tris = []
    for n in range(1, max_val+1):
        tris.append(int(0.5 * n * (n + 1)))
    return tris


tris = calc_tris(100000)
pents = calc_pents(65000)
hexes = calc_hexes(60000)
for num in hexes:
    if num in pents and num in tris and num > 40755:
        print(num)
        break
