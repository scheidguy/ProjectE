# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:34:04 2020

@author: schei
"""


import random

N = 4
turns = 10000000
# dice=[2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]
dice=[2,3,3,4,4,4,5,5,5,5,6,6,6,7,7,8]
landed = [0 for i in range(40)]
current = 0
turn = 0
doubles = 0
while turn < turns:
    turn += 1
    if turn % 1000000 == 0:
        print(f'Rolls: {turn}')

    roll = dice[random.randint(0, N**2 - 1)]

    if N == 6:
        if roll == 2 or roll == 12:
            doubles += 1
        elif roll == 4 or roll == 10:
            if random.randint(1, 3) == 1:
                doubles += 1
            else:
                doubles = 0
        elif roll == 6 or roll == 8:
            if random.randint(1, 5) == 1:
                doubles += 1
            else:
                doubles = 0
        else:
            doubles = 0
    elif N == 4:
        if roll == 2 or roll == 8:
            doubles += 1
        elif roll == 4 or roll == 6:
            if random.randint(1, 3) == 1:
                doubles += 1
            else:
                doubles = 0
        else:
            doubles = 0
    else:
        print('IMPLEMENT NEW DOUBLES LOGIC')
        break

    if doubles == 3:
        doubles = 0
        current = 10
        landed[current] += 1
        continue

    if current + roll >= 40:  # must've passed go
        current -= 40

    if current + roll in [2, 17, 33]:  # community chest
        card = random.randint(1, 16)
        if card == 1:
            current = 0
        elif card == 2:
            current = 10
        else:
            current += roll
    elif current + roll in [7, 22, 36]:  # chance
        card = random.randint(1, 16)
        if card == 1:
            current = 0
        elif card == 2:
            current = 10
        elif card == 3:
            current = 11
        elif card == 4:
            current = 24
        elif card == 5:
            current = 39
        elif card == 6:
            current = 5
        elif card == 7 or card == 8:
            if current + roll == 7:
                current = 15
            elif current + roll == 22:
                current = 25
            elif current + roll == 36:
                current = 5
            else:
                print('CATASTROPHIC ERROR')
        elif card == 9:
            if current + roll == 22:
                current = 28
            else:
                current = 12
        elif card == 10:
            current += roll - 3
        else:
            current += roll
    elif current + roll == 30:  # JAIL MUTHAFUCKA
        current = 10
    else:  # normal roll
        current += roll
    landed[current] += 1
percents = []
for space in landed:
    percents.append(round(100*space/sum(landed), 2))
print(percents[0:10])
print(percents[10:20])
print(percents[20:30])
print(percents[30:40])
