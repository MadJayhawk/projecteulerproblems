"""
Problem #: 34

https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

answer =  40730

---------------------------------------------

from math import factorial

print(sum([i for i in range(10, 10**6) \
      if i == sum(map(factorial, map(int, list(str(i)))))]))

"""
from math import factorial


s=0 
t=0
for num in range(1,50000):
    y=[int(i) for i in str(num)] 
    for i in y:
        s+=factorial(i)
    if num==s and num not in [1,2]:
        t+=s    
    s=0
print(t)