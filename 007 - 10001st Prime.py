'''

Problem #: 7

https://projecteuler.net/problem=7

Difficulty: 5%

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


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
prt('',max(list(primes_upto(10001))))
    



