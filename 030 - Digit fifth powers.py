'''
Problem #: 30

https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

answer = 443,839

'''

from itertools import product

def c(s):
    d=[]
    for i in s:
        d.append(int(i)**5) 
    return d
t=0
for b in product(list('0123456789'), repeat=8):
    s=str(sum(c(b)))
    r=str(''.join(list(b))) 
    if r==s and s not in ['0001','0000']:
        t+=int(s)
print()
print(t)

'''
----------------------------------------------------------------
accumulator = 0
for i in range(2, int(1e6)):
    powersum = sum(map(lambda e: int(e) ** 5, str(i)[:]))
    if powersum == i:
        accumulator += i
print(accumulator)

---------------------------------------------------------------
print(sum([x for x in range(10, 353999) if x == sum([int(i)**5 for i in str(x)])]))
'''