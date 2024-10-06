'''

Problem #: 14

https://projecteuler.net/problem=14

Difficulty: 5%

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

answer = 837799
-------------------------------------------------------
collatz = {1:1}
def Collatz(n):
    global collatz
    if not collatz.has_key(n):
        if n%2 == 0:
            collatz[n] = Collatz(n/2) + 1
        else:
            collatz[n] = Collatz(3*n + 1) + 1
    return collatz[n]

for j in range(1000000,0,-1):
    Collatz(j)

print collatz.keys()[collatz.values().index(max(collatz.values()))] 
---------------------------------------------------
'''

def prt(desc,*args):
    print()
    print(desc,': ',*args)

e=[]
m = 1 
for i in range(1,1000001):
    # i=13
    n=i 
    d=[i] 
    while n !=1:
        if n%2==0:  
            d.append(n//2)  
            n=n//2   
        else: 
            d.append(3*n+1)   
            n=3*n+1
    if len(d)>m:
        m=len(d)
        e.append([len(d),i])
# prt('d',d)
prt('e',e)


