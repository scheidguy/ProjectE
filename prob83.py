# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:15:58 2020

@author: schei
"""


import numpy as np

matrix = []

# matrix.append([131, 673, 234, 103, 18])
# matrix.append([201, 96, 342, 965, 150])
# matrix.append([630, 803, 746, 422, 111])
# matrix.append([537, 699, 497, 121, 956])
# matrix.append([805, 732, 524, 37, 331])

f = open('p083_matrix.txt', 'r')
text = f.readlines()
f.close()
for line in text:
    line = line.split(',')
    for i in range(len(line)):
        line[i] = int(line[i])
    matrix.append(line)

matrix = np.array(matrix)
if matrix[0, 0] == 131:
    size = 5  # toy problem
else:
    size = 80  # real deal

# DJIKSTRA'S ALGORITHM
big = 10**9
minpath = big * np.ones((size, size))  # initialize distances as huge nums
minpath[0, 0] = matrix[0, 0]  # can move any direction, start upper left
visited = np.zeros((size, size))  # keep track of which nodes we've visited
vpaths = big * np.ones((size, size))  # in-between matrix used to find next
vpaths[0, 0] = matrix[0, 0]

row = 0
col = 0
while visited[-1, -1] == 0:
    curr = minpath[row, col]
    left = big + 1
    right = big + 2
    top = big + 3
    bottom = big + 4
    if col != 0:
        if not visited[row, col-1]:
            left = curr + matrix[row, col-1]
            if left < minpath[row, col-1]:
                minpath[row, col-1] = left
                vpaths[row, col-1] = left
    if col != size-1:
        if not visited[row, col+1]:
            right = curr + matrix[row, col+1]
            if right < minpath[row, col+1]:
                minpath[row, col+1] = right
                vpaths[row, col+1] = right
    if row != 0:
        if not visited[row-1, col]:
            top = curr + matrix[row-1, col]
            if top < minpath[row-1, col]:
                minpath[row-1, col] = top
                vpaths[row-1, col] = top
    if row != size-1:
        if not visited[row+1, col]:
            bottom = curr + matrix[row+1, col]
            if bottom < minpath[row+1, col]:
                minpath[row+1, col] = bottom
                vpaths[row+1, col] = bottom
    visited[row, col] = 1
    vpaths[row, col] = big * 2  # never come back
    row = np.unravel_index(np.argmin(vpaths), vpaths.shape)[0]
    col = np.unravel_index(np.argmin(vpaths), vpaths.shape)[1]
print(minpath[-1, -1])
