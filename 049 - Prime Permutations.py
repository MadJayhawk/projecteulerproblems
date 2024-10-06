"""

Problem #: 49

https://projecteuler.net/problem=49

Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Answer:  296962999629
Completed on Tue, 11 Jan 2022, 15:58
"""
import itertools
from sympy import sieve

prime_gen = sieve.primerange(1000, 10000)
p = [str(i) for i in list(prime_gen)]
f = []
for k in p:
    for i in list(itertools.permutations(k)):
        t = "".join(i)
        if t not in f and t in p:
            f.append(t)
g = sorted(f)

for i in range(0, len(g)):
    for j in range(i + 1, len(g)):
        r = 2 * int(g[j]) - int(g[i])
        if r > 10000:
            break
        if (
            str(r) in g
            and sorted(g[i]) == sorted(g[j]) == sorted(str(r))
            and g[i] != "1487"
        ):
            print(g[i] + g[j] + str(r))
