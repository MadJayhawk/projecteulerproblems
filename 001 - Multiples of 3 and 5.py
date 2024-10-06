'''
Problem #: 1

https://projecteuler.net/problem=1

Difficulty: 5%

Answer:  233168

Completed on Wed, 15 Mar 2023, 21:14
'''

d=0
for i in range(0,1000):
    if i%3==0 or i%5==0 :
        d+=i
print('sum',d) 