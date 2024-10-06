'''

Problem #: 16

https://projecteuler.net/problem=16

Difficulty: 5%

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

Answer = 1366

-------------------------------------------------------
sum = 0
for n in str(2**1000):
	sum += int(n)
print sum

'''

def prt(*args):
    print()
    if args[0]=='':
        print(*args)
    else:
        print(args[0],': ',*args) 


prt('',sum([int(i) for i in str(2**1000)]))



