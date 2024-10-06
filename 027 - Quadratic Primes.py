'''
Problem #: 27

https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

n**2 + n +41

It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible by 41, and certainly when  is clearly divisible by 41.

The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2 + a*n + b

, where |a|<1000  and |b|<=1000

where  is the modulus/absolute value of 

e.g. |11| = 11 and |-| = 4 and 

Find the product of the coefficients, a and b
, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0 .

Answer =   -59231

'''
#  https://www.youtube.com/watch?v=3MsmbDDIRg8


from sympy import primerange,isprime
prime_count=0
for a in range(-1000,1000):
    for b in primerange(1,1000): 
        aux_prime_count =0
        n=0
        while isprime(n ** 2 + a *n +b):
            aux_prime_count+=1
            n+=1
        if aux_prime_count > prime_count:
            prime_count = aux_prime_count
            amax = a
            bmax = b
print(amax*bmax)
  
