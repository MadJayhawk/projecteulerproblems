"""

Problem #: 46

https://projecteuler.net/problem=46

Distinct Primes Factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

Answer:  134043
Completed on Mon, 20 Dec 2021, 07:36

time:  1099.112 seconds

"""


def pollard_rho(n):
    d = []
    for i in range(2, n + 1):
        if n % i == 0:
            count = 1
            for j in range(2, (i // 2 + 1)):
                if i % j == 0:
                    count = 0
                    break
            if count == 1:
                d.append(i)
    return len(d)


c = 0
answer = 0
for i in range(500, 1000000):
    if pollard_rho(i) == 4:
        c += 1
        # print(i, c)
        if c == 4:
            answer = i - 3
            break
    else:
        c = 0
print(f"{answer = }")
