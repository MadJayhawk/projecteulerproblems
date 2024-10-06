'''

Problem #: 6

https://projecteuler.net/problem=6

Difficulty: 5%

Answer:  25164150
Completed on Wed, 15 Mar 2023, 21:26

The sum of the squares of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

def prt(desc,*args):

    print()
    print(desc,': ',*args)
s=0
sm=0
for i in range(101): 
    s+=i**2
    sm+=i
sm=sm**2
prt('sum of the squares',s)
prt('square of the sum',sm)
prt('difference',sm-s)
