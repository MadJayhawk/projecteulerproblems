'''

Problem #: 37

https://projecteuler.net/problem=37

Difficulty: 5%

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
 from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

answer = 7848317
-------------------------------------------------------------
def isPrime(k):
    """Only available for odd numers."""
    if all(list(k%p != 0 for p in range(3, int(k/3) + 1, 2))):
        return(True)
    else:
        return(False)
    
def isLeftTrunc(k):
    T = [k]
    for i in range(2, len(str(k))):
        T.append(k%(10**i))
    if all(list(isPrime(t) for t in T)):
        return(True)
    else:
        return(False)



Head = [2, 3, 5, 7]         # one-digit primes

Trunc = []


while len(Trunc) < 11:
    NewH = []
    for h in Head:
        for i in [3, 7]:            # only possibilities for truncatable numbers
            if isPrime(h * 10 + i):
                NewH.append(h * 10 + i)
                if isLeftTrunc(h * 10 + i):
                    Trunc.append(h * 10 + i)
        for i in [1, 9]:            # other possibilities for primes
            if isPrime(h * 10 + i):
                NewH.append(h * 10 + i)
    Head = NewH

print(sum(Trunc))
'''

from sympy import sieve
fp = list(sieve.primerange(2, 1000000))
cnt=0
tf=[True]
for r in range(11,1000000,2):  
    a=str(r)
    if r in fp:
        k=0
        for i in range(1,len(a)+1): 
            if int(a[0:i]) not in fp or int(a[k:]) not in fp:
                tf.append(False)
                break
            k=k+1
        if all(tf):
            cnt+=r
    tf=[True]
print(cnt)