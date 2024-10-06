"""
Problem #: 46

https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1**2
15 = 7 + 2*2**2
21 = 3 + 2*3**2
25 = 7 + 2*3**2
27 = 19 + 2*2**2
33 = 31 + 2*1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Answer:  5777
Completed on Sun, 19 Dec 2021, 12:17

Took 330.7 milliseconds

"""

from sympy import sieve
from fastnumbers import isintlike
import math
from time import time

t0 = time()
primes = list(sieve.primerange(3, 10000))
composites = []
for i in range(4, 10000):
    if i not in primes and i % 2 != 0:
        composites.append(i)
for i in composites:
    for j in primes:
        if j < i:
            try:
                s = math.sqrt((i - j) / 2)
                t = not (isintlike(math.sqrt((i - j) / 2)))
                if t == False:
                    break
            except:
                pass
        else:
            print(f"\n answer = {i}")
            print(f"\n It took {(time() - t0) * 1000} milliseconds.")
            quit()
