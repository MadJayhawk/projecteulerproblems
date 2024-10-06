"""
Problem #: 35

https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

answer = 55

----------------------------------------------

import numpy as np 
from more_itertools import circular_shifts

def Erat(N):
  if N == 0 or N == 1 : return []
  elif N == 2: return [2]
  elif N == 3: return [2,3]
  else:
    N_bool = np.array([True]*(N+1))
    N_bool[0] = False
    N_bool[1] = False
    N_bool[2] = True
    N_bool[3] = True
    N_bool[2**2::2] = False 
    p = 3
    while p*p <= N:
      N_bool[p**2::p] = False
      p = p + 2
      while not N_bool[p]: p = p + 2
  return list(np.nonzero(N_bool)[0]) 
  
primes = set(Erat(10**6))
primes = primes - {2,3,5,7}
circ = {2,3,5,7}
while primes:
  p = primes.pop()
  primes.add(p) # will need it for primes check
  cshifts = {int(''.join(u)) for u in circular_shifts(str(p))}
  cs = True
  for c in cshifts:
    if c not in primes:
      cs = False
      break
  if cs:
    circ |= cshifts
    primes -= cshifts
  else:
    primes.remove(p)
print(len(circ))
print(sorted(list(circ)))
"""
from itertools import permutations
from itertools import compress

def rotate_it(h):
    # print(h)
    k=str(h)
    d=[]
    for j in range(0,len(k)):
        f=k[1:len(h)]+k[0]
        # print(k)
        d.append(int(f))
        k=f
    # print(d)
    return d

def fast_primes(n):
    if n <= 2:
        return []
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    primes = list(compress(range(1, n, 2), sieve))
    primes[0] = 2
    return primes
 
fp=fast_primes(1000000)
# print(fp,'\n')

d=[]
for i in range(1,1000000):
    a=sorted(rotate_it(str(i)))
    if a not in d: 
        d.append(sorted(a))
cnt=0
for i in d:
    a=True
    for j in i:
        # print(j,len(str(j)))

        if j not in fp and a:
            a=False
    if a: 
        cnt+=len(i)
        print(i,cnt)
        
print(cnt-1)  # 11 is counted twice
