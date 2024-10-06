"""

Problem #: 48

https://projecteuler.net/problem=48

Self Powers

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

Answer:  9110846700
Completed on Mon, 20 Dec 2021, 07:49

"""
sum_of_squares = 0
for num in range(1, 1001):
    sum_of_squares += num ** num
r = str(sum_of_squares)
g = len(r)
answer = r[-10:]

print(f" {answer = }")

"""
str(sum([i**i for i in range(1,1001)]))[-10:]


"""
