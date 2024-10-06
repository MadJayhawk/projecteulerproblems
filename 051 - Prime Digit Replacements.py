"""
Prime Digit Replacements

Problem #: 51    Started:  4/10/2022  Finished:  4/21/2022

https://projecteuler.net/problem=51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56z3. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

Answer:  121313
Completed on Thu, 21 Apr 2022, 09:26


"""
from sympy import isprime
import itertools as it
import re

# patterns     ['&&.', '&.&', '&..', '.&&', '.&.', '..&']
def patterns_from_list(lst, n):
    d = set()
    for c in it.permutations(lst, n):
        d.add("".join(str(b) for b in c))
    return sorted(
        list(x for x in list(x for x in d if x.count("&") > 0) if x.count("&") < n)
    )


# ['&12', '&13', '&14', '&15', '&16', '&17', '&18', '&19', '&10', '&21', '&23', '&24', '&25', '&26'
def create_list_values(n):
    a = "&1234567890"
    x = list(it.product(a, repeat=n))
    d = []
    for i in x:
        tt = "".join(i)
        if 0 < tt.count("&") < n:
            d.append(tt)
    return d


#  sorts data into families ie '1x23x4' family based on value of pattern ie '.&..&.'
# there are 10 families '&&...','&.&..', etc  generated
# patterns=['&&[0-9]', '&[0-9]&', '&[0-9][0-9]', '[0-9]&&', '[0-9]&[0-9]', '[0-9][0-9]&']
def sort_into_families(lst, patterns):
    # Filter out all elements that match the above pattern
    family = []
    d = []
    for i in patterns:

        for x in lst:
            y = re.match(i, x)
            if y != None:
                d.append(y[0])
        family.append(d)
        d = []
    e = []
    for i in family:
        e.append(sorted(list(set(i))))
    return e


x = []
for i in range(10):
    x.append("[0-9]")
    x.append("&")

n = 6

patterns = patterns_from_list(x, n)  # ['&&[0-9]', '&[0-9]&', '&[0-9][0-9]', '[0-9]&&',]
values = sorted(create_list_values(n))  # ['&12', '&13', '&14', '&15', '&16',
families = sort_into_families(values, patterns)

k = 0
hh = {}
for i in families:
    k += 1
    d = []
    for j in i:
        for m in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            res_str = int(re.replace(r"\&", m, j))
            if res_str not in d and isprime(res_str) and res_str > 99999:
                d.append(res_str)
        hh[j] = d
        d = []
for i, j in hh.items():
    if len(j) == 8:
        print(f"{i}  {min(j)}  {j}", "\n")
