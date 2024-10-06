'''

Problem #: 3

https://projecteuler.net/problem=3

Difficulty: 5%

Answer:  6857
Completed on Wed, 15 Mar 2023, 21:19

'''

def prt(desc,*args):
    print()
    print(desc,': ',*args)  

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2) 
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors
print(prime_factors(600851475143))