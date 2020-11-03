# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 00:04:39 2020

@author: schei
"""


# ONLY DIGITS NEAR THE END MATTER FOR CALCULATING PRODUCT
# after calculating 2**7830457, convert to string
num = 28433
power = 2**7830457
pstr = str(power)
prod = num * int(pstr[-25:]) + 1
print(str(prod)[-10:])
