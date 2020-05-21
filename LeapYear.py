#!/bin/python3
# Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the day of the year) during a year in the inclusive range from to

# .

# From
# to , Russia's official calendar was the Julian calendar; since they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in , when the next day after January was February . This means that in , February was the

# day of the year in Russia.

# In both calendar systems, February is the only month with a variable amount of days; it has
# days during a leap year, and days during all other years. In the Julian calendar, leap years are divisible by

# ; in the Gregorian calendar, leap years are either of the following:

#     Divisible by 

# .
# Divisible by
# and not divisible by

#     .

# Given a year,
# , find the date of the day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is

# .

# For example, the given
# . is divisible by , so it is a leap year. The day of a leap year after is September 12, so the answer is

# .

# Function Description

# Complete the dayOfProgrammer function in the editor below. It should return a string representing the date of the

# day of the year given.

# dayOfProgrammer has the following parameter(s):

#     year: an integer

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if(year == 1918):
        return('26.09.1918')
    if(year < 1918):
        if(year % 4 == 0):
            rtn = '12.09.'+str(year)
            return (rtn)
        else:
            rtn = '13.09.'+str(year)
            return (rtn)
    
    else:
        if (year%400 == 0 or (year % 4 == 0 and year % 100!=0)):
            rtn = '12.09.'+str(year)
            return (rtn)
        else:
            rtn = '13.09.'+str(year)
            return(rtn)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
