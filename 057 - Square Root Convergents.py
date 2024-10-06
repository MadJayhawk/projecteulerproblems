'''
Square root convergents


Problem 57

Started:  12/13/22 2:20pm


Answer:  153
Completed on Wed, 14 Dec 2022, 16:08


It is possible to show that the square root of two can be expressed as an infinite continued fraction.



By expanding this for the first four iterations, we get:





The next three expansions are
,
, and
, but the eighth expansion,

, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
'''

def sq_root_conv(a,b):
    return 2*b+a,a+b
a=3
b=2
cnt=0
# print(sq_root_conv(a,b))
for i in range(1001):
    a,b=sq_root_conv(a,b)
    if len(str(a))>len(str(b)):
        cnt+=1
print(f'The answer is {cnt}')