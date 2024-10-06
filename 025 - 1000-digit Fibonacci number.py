'''
Problem #: 25

https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Answer:  4782
Completed on Wed, 26 May 2021, 20:04 

------------------------------------------
nums = [1, 1]
while len(str(nums[len(nums)-1])) < 1000:
    nums.append(nums[len(nums)-1] + nums[len(nums)-2])

print(len(nums)+1)
--------------------------------------------
i, j, term = 0, 1, 2
while True:
    fib = i+j
    if len(str(fib)) >= 1000:
        print term, ":", fib
        break
    i, j, term = j, fib, term+1
-----------------------------------------

'''
def prt(*args): 
    print()  
    print(*args)

def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b


for index, number in enumerate(fibo()):
    if len(str(number)) == 1000:
        print(index)
        break