'''

Problem #: 10
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer:  142913828922
Completed on Fri, 17 Mar 2023, 10:06


Difficulty: 5 
'''

def prt(desc,*args):
    print()
    print(desc,': ',*args)


def primes_upto(limit):
    prime = [True] * limit
    for n in range(2, limit):
        if prime[n]:
            yield n # n is a prime
            for c in range(n*n, limit, n):
                prime[c] = False 
prt('',sum(list(primes_upto(2000000))))