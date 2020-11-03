# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:24:16 2020

@author: schei
"""


tri = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split('\n')

# tri = '''3
# 7 4
# 2 4 6
# 8 5 9 3'''.split('\n')

for ind1 in range(len(tri)):
    tri[ind1] = tri[ind1].split(' ')
    for ind2 in range(len(tri[ind1])):
        tri[ind1][ind2] = int(tri[ind1][ind2])


# DIFFERENT STRATEGY:
# 1. start at top, and find optimal path from each successive row
# 2. store pathsum in a similarly indexed list as we go

pathsum = [[tri[0][0]]]
for row in range(1, len(tri[-1])):
    rowsum = []
    for col in range(len(tri[row])):
        val = tri[row][col]
        if col == 0:  # far left branch
            rowsum.append(val + pathsum[row-1][col])
        # far right branch
        elif col == len(tri[row]) - 1:
            rowsum.append(val + pathsum[row-1][col-1])
        # optimal to go up and right from here
        elif pathsum[row-1][col] > pathsum[row-1][col-1]:
            rowsum.append(val + pathsum[row-1][col])
        # optimal to go up and left from here
        else:
            rowsum.append(val + pathsum[row-1][col-1])
    pathsum.append(rowsum)

print(max(pathsum[-1]))


# # STRATEGY:
# # 1. start at bottom left
# # 2. determine if ever optimal to end here (check if both sides are greater)
# # 3. continue up if optimal, otherwise try other branch
# # 4. record value if reached the top
# for base in range(len(tri[-1])):
#     col = base
#     row = len(tri) - 1
#     still_climbing = True
#     while still_climbing:
#         val = tri[row][col]
#         if col == 0:
#             if val < tri[row][col+1]:
#                 col += 1
#                 break  # on far left and less than neighbor to right
#         elif col == len(tri[row]) - 1:
#             if val < tri[row][col-1]:
#                 row -= 1  # move up
#                 break  # on far right and less than neighbor to left
#         elif val < tri[row][col+1] and val < tri[row][col-1]:
#             col += 1
#             break  # somewhere in middle and less than both neighbors
#         row -= 1  # move up
#         if row == 0:  # made it to the top!
