'''

Problem #: 17

https://projecteuler.net/problem=17

Difficulty: 5%

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out  numbers is in compliance with British usage.

Answer:  21124
Completed on Sun, 16 May 2021, 07:58
 
'''
from num2words import num2words

def prt(*args):
    print() 
    print(*args)


total=0
for i in range(1,1001):
    b=num2words(i)
    total+=len(b)-(0,1)['-' in b]-b.count(' ')
print(f'total: {total}')



