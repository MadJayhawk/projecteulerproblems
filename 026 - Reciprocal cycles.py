'''
Problem #: 26

https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Answer:  983
Completed on Fri, 11 Jun 2021, 22:22 

https://www.geeksforgeeks.org/find-length-period-decimal-value-1n/

'''
def getPeriod( n) :
    rem = 1 
    for i in range(1, n + 2):
        rem = (10 * rem) % n
    d = rem
    count = 0
    rem = (10 * rem) % n
    count += 1
    while rem != d :
        rem = (10 * rem) % n
        count += 1   
    return count
if __name__ == "__main__":
    h=0
    n=0
    for i in range(10,1001):
        x=getPeriod(i)
        if x>h:
            h=x
            n=i
    print(n)