'''
Spiral primes

Problem 58

Started: 14 Dec 2022, 16:08

Answer:  26241
Completed on Fri, 16 Dec 2022, 11:44


    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

    If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?


'''
from gmpy2 import is_prime


t=1
s=0
x=1
sides=1
for v in range(2,1000000,2):
    sides+=2
    for i in range(0,4):
        x+=v
        t+=1
        if is_prime(x):
            s+=1
    if s/t<.1:
        print(f'The answer is {sides}')
        break

'''

import string, itertools
code = eval(open('cipher1.txt').read())

def best_match(code):
    good_chars=set(map(ord, string.ascii_letters) + [ord(" ")])
    maxscore=0
    bestletter=None
    for letter in map(ord,string.lowercase):
        score = 0
        for c in code:
            if (c ^ letter) in good_chars:
                score += 1
        if score > maxscore:
            maxscore   = score
            bestletter = letter
    return bestletter

pad = [best_match(code[::3]), best_match(code[1::3]), best_match(code[2::3])]

print sum((ch ^ p) for (ch,p) in zip(code, itertools.cycle(pad)))
'''