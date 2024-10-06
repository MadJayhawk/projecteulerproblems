'''
Problem #: 32

https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

answer = 45228 
------------------------------------------------------
def pandigital(x: int, y: int) -> bool:
    string_number = str(x) + str(y) + str(x * y)            
    for i in range(1,10):
        if len(string_number) != 9 or str(i) not in string_number:
            return False    
    pandigital_set.add(x * y)
    return True


pandigital_set = set()

for i in range(1, 10):
    for j in range(1000, 10000):        
        pandigital(i, j)
              
for i in range(10, 100):
    for j in range(100, 1000):        
        pandigital(i, j)
            
print(sum(pandigital_set))
--------------------------------------------------
products = set()
pandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for x_limit, y_limit in [(9, 10000), (100, 1000)]:
    for x in range(x_limit):
        for y in range(y_limit):
            product = x * y
            if sorted(str(x) + str(y) + str(product)) == pandigital:
                products.add(product)

print(sum(products))

'''
# Find all the unique 4 digit permutations of '123456789'
# Determine the identity of each permutation:  7254 --> 13689
# Calculate the factors of 7254 and find their identity : 39 x 186 ---> 13689
#    and determine if equal to the identity of the permutation

from itertools import permutations
import re

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p 
            yield ''.join(list(p))
d={}
t=0
for p in unique_permutations('123456789', 4):
    if p not in d: 
        dx=[]
        for match in re.finditer(r"[^"+re.escape(p)+r"]", "123456789", re.MULTILINE):
            dx.append(match.group())    
        q=''.join(sorted(dx))     
        fac=list([str(i),str(int(p)//i)] for i in range(1, int(int(p)**0.5) + 1) if int(p) % i == 0)
        k=[]
        for jj in fac:
            cc=''.join(sorted(jj[0]+jj[1] )) 
            if '0' not in cc and len(cc)==len(set(cc)): 
                k.append(cc)     
        if q in k:
            t=t+int(p)
print(t)