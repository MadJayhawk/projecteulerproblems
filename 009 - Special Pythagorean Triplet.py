'''

Problem #: 9

https://projecteuler.net/problem=9

Difficulty: 5%

Answer:  31875000
Completed on Wed, 15 Mar 2023, 21:37

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
 
There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

'''

def prt(desc,*args):
    print()
    print(desc,': ',*args)

Looked up values on https://www.wolframalpha.com/input/?i=1000%3Da%2Bb%2Bc%2C+a**2+%2B+b**2+%3Dc**2

Answer 200**2 + 375**2 = 425**2
        200 + 375 + 425 = 1000
        200 * 375 * 425 = 31875000