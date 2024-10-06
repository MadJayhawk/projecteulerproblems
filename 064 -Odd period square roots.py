'''
Odd period square roots


Problem 64

Started on 17 March 2023

Completed on Sat, 18 Mar 2023, 07:14

Answer:  1322

Used ChatGPT to get function that calculated (in the loop) the continued fraction.  ChatGPT had a difficult time handling perfect squares.
'''
import math

def continued_fraction(n):
    a0 = int(math.sqrt(n))
    if a0**2 == n:
        return [a0]
    result = [a0]
    a, p, q = a0, 0, 1
    while a != 2*a0:
        p = a*q - p
        q = (n - p**2)/q
        a = int((a0 + p)/q)
        result.append(a)
    if (len(result)-1)%2!=0:
        return 'odd'
    return 'even'
cnt=0
for i in range(0,10000):
    if continued_fraction(i)=='odd':cnt+=1
print(f'The answer is {cnt}')
