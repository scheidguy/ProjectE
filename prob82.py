# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:22:18 2020

@author: schei
"""


import numpy as np

matrix = []

# matrix.append([131, 673, 234, 103, 18])
# matrix.append([201, 96, 342, 965, 150])
# matrix.append([630, 803, 746, 422, 111])
# matrix.append([537, 699, 497, 121, 956])
# matrix.append([805, 732, 524, 37, 331])

f = open('p082_matrix.txt', 'r')
text = f.readlines()
f.close()
for line in text:
    line = line.split(',')
    for i in range(len(line)):
        line[i] = int(line[i])
    matrix.append(line)

matrix = np.array(matrix)
if matrix[0][0] == 131:
    size = 5  # toy problem
else:
    size = 80  # real deal

minpath = np.zeros((size, size))
minpath[:, 0] = matrix[:, 0]  # can only move right up and down

for col in range(1, size):
    # Find minpath to top of new column
    best = minpath[0, col-1] + matrix[0, col]
    for row in range(1, size):
        if minpath[row, col-1] + sum(matrix[0:row+1, col]) < best:
            best = minpath[row, col-1] + sum(matrix[0:row+1, col])
    minpath[0, col] = best

    for row in range(1, size):
        left = minpath[row, col-1] + matrix[row, col]
        top = minpath[row-1, col] + matrix[row, col]
        bottom = 10**10  # initialize as a huge number
        for r in range(row+1, size):
            if minpath[r, col-1] + sum(matrix[row:r+1, col]) < bottom:
                bottom = minpath[r, col-1] + sum(matrix[row:r+1, col])
        if left <= top and left <= bottom:
            minpath[row, col] = left
        elif top <= left and top <= bottom:
            minpath[row, col] = top
        else:
            minpath[row, col] = bottom
print(min(minpath[:, -1]))
