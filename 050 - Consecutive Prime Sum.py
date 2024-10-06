"""
Problem #: 50    Started:  1/11/2022

https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Answer:  997651
Completed on Sun, 10 Apr 2022, 16:20

"""

import sieve

m = 1000
p = [i for i in list(sieve.primerange(1, m))]
s, j, cnt, h = (0, 0, 0, 0)
hh = []
while p[j] + p[j + 1] < m:
    s += p[j]
    cnt += 1
    if s in p and cnt > h:
        h = cnt
        answer = s
    j += 1
    if s > m:
        j, s, cnt = (0, 0, 0)
        p = p[1:]
print(answer)
