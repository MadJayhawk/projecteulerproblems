'''
Problem #: 24

https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer:  2783915460
Completed on Wed, 26 May 2021, 19:55 

'''
def prt(*args): 
    print()  
    print(*args)

from itertools import permutations
n='0123456789'
p= permutations(n,len(n))
for i,j in enumerate(sorted(list(p))):
    print(i,''.join(j))
    if i >1000002:
        break