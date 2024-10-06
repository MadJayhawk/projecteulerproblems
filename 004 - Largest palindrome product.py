'''

Problem #: 4

https://projecteuler.net/problem=4

Difficulty: 5%

Answer:  906609
Completed on Wed, 15 Mar 2023, 21:21

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def prt(desc,*args):
    print()
    print(desc,': ',*args) 

def is_palindrome(x):
    b=str(x)
    return b[0:3]==b[3:][::-1]

nm=0
for i in range(1,1000):
    for j in range(1,1000) :   
        a=i*j
        if is_palindrome(a):
            if a>nm:
                nm=a
print('',nm)
