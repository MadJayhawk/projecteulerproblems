'''
Problem #: 19

https://projecteuler.net/problem=19



You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Difficulty: 5%

Answer:  171
Completed on Tue, 18 May 2021, 09:59

'''
#Python 3.8.5

import datetime 

Number_of_Sundays = 0
day=1  # first day of the month

for i in range(1901,2001):
    year=i
    for month in range(1,13):
        if datetime.datetime(year, month, day).weekday()==1:  # 1 = Sunday
            Number_of_Sundays+=1

print(f'Number of Sundays between 1/1/1901 and 1/1/2001:  {Number_of_Sundays}')