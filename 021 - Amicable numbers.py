'''
Problem #: 21

https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer:  31626
Completed on Fri, 21 May 2021, 10:13

'''
from functools import reduce

def prt(*args):
    print() 
    print(*args) 

def factors(n): 
    return sorted(list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
p={0:1}
d=set()
for i in range(1,10001):
    p[i]=1
for i in range(1,10001):
    a=factors(i)
    # prt(a,a[:-1])
    if a[:-1]!=[1]:
        b=sum(a[:-1]) 
        if b<10001:
            d.add(b)
            p[i]=b
    else:
        p[i]=1
sm=0
for i in range(2,10001):
    if i==p[p[i]] and p[i]!=p[p[i]]:
        # prt(i,p[i],p[p[i]])
        sm+=i
prt(f'The sum of the amicable numbers between 1 and 10,001: {sm}')

