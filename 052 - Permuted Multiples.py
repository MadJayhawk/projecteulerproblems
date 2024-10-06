"""
Permuted Multiples

Problem #: 52    Started: 4/21/2022

https://projecteuler.net/problem=52


It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Answer:  142857
Completed on Sat, 23 Apr 2022, 10:39

"""
import time


def num_to_list(n, m):
    t = True
    if sorted([int(i) for i in str(n)]) not in m:
        t = False
    return t


start = time.perf_counter()
for i in range(125870, 200000):
    s = [sorted([int(j) for j in str(i)])]
    cnt = 0
    for k in [2, 3, 4, 5, 6]:
        b = num_to_list(i * k, s)
        if not b:
            break
        else:
            cnt += 1
            if cnt == 5:
                print(f"Answer is: {i} \n")
                print("Time taken = %.2f" % (time.perf_counter() - start))
"""
https://projecteuler.net/thread=52&page=2#3825

def f(n): return sorted([int(n) for n in str(n)])
[n for n in range(1,1000000) if f(n)==f(n*2)==f(n*3)==f(n*4)==f(n*5)==f(n*6)]
------------------------------
https://projecteuler.net/thread=52;page=3
def main():
    from itertools import count
    from sets import Set

    for i in count(1):
        if Set(str(2*i)) == Set(str(3*i)) == Set(str(4*i)) == Set(str(5*i)) == Set(str(6*i)):
            print i
            break
main()
------------------------------------
n = 1
while True:
	if sorted(list(str(n*2))) == sorted(list(str(n*3))) == sorted(list(str(n*4))) == sorted(list(str(n*5))) == sorted(list(str(n*6))):
		print "\n".join(["#%i => %s" % (i+1, str(x)) for i, x in enumerate([n, n*2, n*3, n*4, n*5, n*6])])
		break
	n += 1
"""
