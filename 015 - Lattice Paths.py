'''

Problem #: 15

https://projecteuler.net/problem=15

Difficulty: 5%

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

Answer = 137846528820

-------------------------------------------------
import math
# squaring result of 20! to save recalculating 20!
answer = int(math.factorial(40) / (math.factorial(20) ** 2))
print (answer)

'''

def prt(*args):
    print()
    if args[0]=='':
        print(*args)
    else:
        print(args[0],': ',*args)


def fact(n):
    factorial = 1 
    for i in range(1,n + 1):
        factorial = factorial*i
    return factorial
sides=4  # number of sides
answer= fact(sides*2)//fact(sides)**2
prt('',answer)
