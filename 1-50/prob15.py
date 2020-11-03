# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:15:10 2020

@author: schei
"""
# 1, 1, 2, 5, 14, 42    OR    (dim-2)**2 + (dim-3)**2 + ...
# 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756, 705432, 2704156, 10400600, 40116600
# 2*(n-1) + 2*(n-2) + ... + 2 ** (dim-1)
# paths = [2]
# for dim in range(1, 20):
#     numpaths = 2*()


from copy import deepcopy


def calc(row, col, grid):
    if row >= len(grid) or col >= len(grid[0]):
        return 0  # Off of grid
    elif row == len(grid)-1 and col == len(grid[0])-1:
        return 1  # Reached bottom right corner
    else:  # Update grid
        grid[row][col] = 1
        grid_down = deepcopy(grid)
        grid_right = deepcopy(grid)
        return calc(row+1, col, grid_down) + calc(row, col+1, grid_right)


def moving(dim):
    grid = [[0]*dim] * dim
    return calc(0, 0, grid)


mult = 3
num = 6
denom = 3
for dim in range(3, 21):
    mult += 1/denom
    denom += dim
    num *= mult
    print(f'{dim}x{dim}: {num} paths')
