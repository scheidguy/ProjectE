# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:48:20 2020

@author: schei
"""


numways = 1  # start with trivial 2pound coin
for one in range(201):
    print(one)
    for two in range(101):
        for five in range(41):
            for ten in range(21):
                for twenty in range(11):
                    for fifty in range(5):
                        for pound in range(3):
                            if one + 2*two + 5*five + 10*ten + 20*twenty + 50*fifty + 100*pound == 200:
                                numways += 1
print(numways)
