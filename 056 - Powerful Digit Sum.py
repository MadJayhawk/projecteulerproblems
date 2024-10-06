'''
Powerful digit sum

Problem 56

Started:  12-13-22

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

Answer:    972
Completed on Tue, 13 Dec 2022, 13:45

    '''
g=0
for a in range(100):
    for b in range(100):
        n=a**b
        sum_digits = lambda n: 0 if n == 0 else (n % 10) + sum_digits(n // 10)
        s=sum_digits(n)
        if s>g: g=s
print(f'The answer is {g}')

#  Time Elapsed:  1.6414402999944286 seconds