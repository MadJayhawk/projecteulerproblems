"""
Problem #: 33

https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

answer = 100

https://blog.dreamshire.com/project-euler-33-solution/

Just generate all fractions with 2 digit numerators and denominators and ignore ‘trivial’ examples. 
--------------------------------------------

The fraction must have the form: 
 
 10*a+c / 10*c+b with 0<<a<b<c<10


from math import gcd

n, d = 1, 1
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            ac, cb = 10 * a + c, 10 * c + b
            if ac * b == cb * a:
                print(f"{ac}/{cb} - {c}")
                n, d = n * ac, d * cb

print(f"The value of the denominator is {d // gcd(n, d)}")
------------------------------------------
"""
d = 1
for i in range(1, 10):
    for j in range(1, i):
        q, r = divmod(9*j*i, 10*j-i)
        if not r and q <= 9:
            d*= i/float(j)
 
print ("Project Euler 33 Solution =", d)