'''
Problem #: 40

https://projecteuler.net/problem=40


An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Answer:  210
Completed on Mon, 20 Mar 2023, 20:49
'''

def generator2():
    for i in range(0,1000001):
        yield i 
def generator():
    yield from generator2()
q=generator()
b=''.join(map(str,list(q)))
answer=int(b[1])*int(b[10])*int(b[100])*int(b[1000])*int(b[10000])*int(b[100000])*int(b[1000000])
print(answer)
'''
longnum = "".join([str(i) for i in range(1, 1000001)])
positions = [0, 9, 99, 999, 9999, 99999, 999999]
digits = [int(longnum[i]) for i in positions]
product = 1
for i in digits:
    product *= i
print(product)
-------------------------------------
d = '1'
for i in range (2,10**6 + 1):
    i = str (i)
    d += i

result = int(d[0])*int(d[10-1])*int(d[100-1])*int(d[1000-1])*int(d[10000-1])*int(d[100000-1])*int(d[1000000-1])
print (result)
    
'''