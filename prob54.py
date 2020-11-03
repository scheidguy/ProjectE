# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:32:44 2020

@author: schei
"""


def get_hand_rank(r, s):
    kicker = []  # to record any kicker info, if necessary
    r.sort()
    low = min(r)
    straight = [n for n in range(low, low+5)]
    if r == straight and len(set(s)) == 1:  # straight flush
        rank = 8
        kicker.append(max(r))
    elif len(set(r)) == 2:  # 4 of a kind or full house
        if r.count(max(r)) == 1:
            rank = 7
            kicker.append(min(r))
            kicker.append(max(r))
        elif r.count(max(r)) == 4:
            rank = 7
            kicker.append(max(r))
            kicker.append(min(r))
        elif r.count(max(r)) == 3:
            rank = 6
            kicker.append(max(r))
            kicker.append(min(r))
        else:
            rank = 6
            kicker.append(min(r))
            kicker.append(max(r))
    elif len(set(s)) == 1:  # flush
        rank = 5
        kicker.extend(r[::-1])
    elif r == straight:  # straight
        rank = 4
        kicker.extend(r[::-1])
    elif len(set(r)) == 3 or len(set(r)) == 4:  # 3 of a kind or two pairs or 1
        num_pairs = 0
        # if r[-1] == r[-2]:
        #     if r[-1] == 10:
        #         stop = True
        for i in r:
            if r.count(i) == 3:  # 3 of a kind
                rank = 3
                kicker.append(i)
                for no_use in range(3):
                    r.remove(i)
                kicker.extend(r[::-1])
                break
            elif r.count(i) == 2:  # first or second pair
                if num_pairs == 1:
                    if i == first_pair:
                        if i == r[-1]:
                            rank = 1
                            kicker.append(first_pair)
                            r.remove(first_pair)
                            r.remove(first_pair)
                            kicker.extend(r[::-1])
                        continue
                num_pairs += 1
                if num_pairs == 1:
                    first_pair = i
                elif num_pairs == 2:
                    rank = 2
                    if i > first_pair:
                        kicker.append(i)
                        kicker.append(first_pair)
                    else:
                        kicker.append(first_pair)
                        kicker.append(i)
                    r.remove(i)
                    r.remove(i)
                    r.remove(first_pair)
                    r.remove(first_pair)
                    kicker.extend(r)
                    break
            elif i == r[-1]:  # on last iteration, must be just one pair
                rank = 1
                kicker.append(first_pair)
                r.remove(first_pair)
                r.remove(first_pair)
                kicker.extend(r[::-1])
                break
    else:  # high card
        rank = 0
        kicker.extend(r[::-1])
    kicker.insert(0, rank)

    return kicker


def which_player_wins(r1, r2, s1, s2):
    # may need to handle Ace = 1 and Ace = 14, it's unclear, assume not for now
    this_player = 2
    hand1 = get_hand_rank(r1, s1)
    hand2 = get_hand_rank(r2, s2)
    for ind in range(len(hand1)):
        if hand1[ind] > hand2[ind]:
            this_player = 1
            break
        elif hand2[ind] > hand1[ind]:
            break
    return this_player


f = open('p054_poker.txt', 'r')
text = f.read()
f.close()
hands = text.split('\n')
hands.pop()  # get rid of last blank line
wins = 0
for hand in hands:
    ranks1 = []
    suits1 = []
    ranks2 = []
    suits2 = []
    for i in range(0, len(hand)+1, 3):
        rank = hand[i]
        suit = hand[i+1]

        if rank == 'A':
            rank = 14
        elif rank == 'T':
            rank = 10
        elif rank == 'J':
            rank = 11
        elif rank == 'Q':
            rank = 12
        elif rank == 'K':
            rank = 13
        else:
            rank = int(rank)

        if suit == 'C':
            suit = 1
        elif suit == 'S':
            suit = 2
        elif suit == 'D':
            suit = 3
        else:  # must be Hearts
            suit = 4

        if len(ranks1) != 5:  # not done grabbing first player's hand yet
            ranks1.append(rank)
            suits1.append(suit)
        else:  # done with first player, time to grab second player's hand
            ranks2.append(rank)
            suits2.append(suit)

    if which_player_wins(ranks1, ranks2, suits1, suits2) == 1:
        wins += 1
print(wins)
