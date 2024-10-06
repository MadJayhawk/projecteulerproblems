"""
Problem #: 41

https://projecteuler.net/problem=41

Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from sympy import prevprime

j = 7654321
k = 7654321
g = "1"
while g != "1234567":
    k = prevprime(j)
    g = "".join(sorted(str(k)))
    j = k
print(" answer = ", k)


"""
from sympy import isprime


def panDigital(n):
    n_digit = len(str(n))
    for x in range(1,n_digit+1):
        if str(x) not in str(n):
            return False
    return True

for x in range(7654321,1,-2):
    if isprime(x) and panDigital(x):
        break
print(x)
---------------------------------------------------------
from itertools import permutations
from sympy import isprime

do_further = True
i=0
while do_further :
    for test in permutations('7654321'[i:]) :
        if isprime(int(''.join(test))) :
            print(''.join(test))
            do_further = False
            break
    i+=1

"""
