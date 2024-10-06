'''
Problem #: 20

Answer:  648
Completed on Sat, 18 Mar 2023, 18:23

https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer:  648
Completed on Tue, 18 May 2021, 13:16

'''
def prt(*args):
    print() 
    print(*args)

import math 

print (f'Sum of the digits in 100!:  {sum([int(x) for x in str(math.factorial(100))])}')

