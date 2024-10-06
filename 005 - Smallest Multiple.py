'''

Problem #: 5

https://projecteuler.net/problem=5

Difficulty: 5%

Answer:  232792560
Completed on Wed, 15 Mar 2023, 21:24

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


'''
d=[]
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True

def prt(desc,*args):
    print()
    print(desc,': ',*args)
a=5040  #2 x 2520  from the problem
for i in range(11,21): 
    if is_prime(i):
        a*=i
print('a',a)
