# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:51:04 2020

@author: schei
"""

monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
til = 6  # start on Jan 1, 1900, which is Monday (6 days from Sunday)
year = 1900
num = 0  # this will keep track of many Sundays on 1st of month

while year < 2001:
    days = 1
    leapflag = False
    yeardays = 365
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leapflag = True
                yeardays = 366
        else:
            leapflag = True
            yeardays = 366
    while days <= yeardays:
        if til == 0:  # It's Sunday!
            if leapflag:
                newmonthflag = False
                for month in range(11):
                    if month == 0:
                        if days - monthdays[month] == 1:
                            newmonthflag = True
                            break
                    else:
                        if days - sum(monthdays[0:month+1]) - 1 == 1:
                            newmonthflag = True
                            break
            else:
                newmonthflag = False
                for month in range(11):
                    if days - sum(monthdays[0:month+1]) == 1:
                        newmonthflag = True
                        break
            if newmonthflag or days == 1:
                if year >= 1901:
                    num += 1
            til = 6
        else:
            til -= 1
        days += 1
    year += 1
print(num)
