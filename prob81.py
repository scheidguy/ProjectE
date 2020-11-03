# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:48:27 2020

@author: schei
"""


import numpy as np

matrix = []
# matrix.append([131, 673, 234, 103, 18])
# matrix.append([201, 96, 342, 965, 150])
# matrix.append([630, 803, 746, 422, 111])
# matrix.append([537, 699, 497, 121, 956])
# matrix.append([805, 732, 524, 37, 331])
f = open('p081_matrix.txt', 'r')
text = f.read().split('\n')
text.pop()
f.close()
for lines in text:
    line = lines.split(',')
    for i in range(len(line)):
        line[i] = int(line[i])
    matrix.append(line)
matrix = np.array(matrix)

minpath = np.zeros((len(text), len(text)))
minpath[0][0] = matrix[0][0]
for i in range(1, len(text)):  # can only move right and down
    minpath[i][0] = matrix[i][0] + minpath[i-1][0]
    minpath[0][i] = matrix[0][i] + minpath[0][i-1]

for row in range(1, len(text)):
    for col in range(1, len(text)):
        top = minpath[row-1][col]
        left = minpath[row][col-1]
        if top < left:
            minpath[row][col] = top + matrix[row][col]
        else:
            minpath[row][col] = left + matrix[row][col]
print(minpath[-1][-1])
