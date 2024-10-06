# 6 kyu  Python
# https://www.codewars.com/kata/5245a9138ca049e9a10007b8/train/python

import itertools


def count_adjacent_pairs(st):
    a = [w.lower() for w in st.split()]
    b = list(list(v) for g, v in itertools.groupby(a))
    return len([c for c in b if len(c) > 1])


if __name__ == "__main__":
    x = "banana banana banana terracotta banana terracotta terracotta pie!"
    print(count_adjacent_pairs(x))
"""
-------------------------------------------------------------------------------
from itertools import groupby
def count_adjacent_pairs(st): 
    return len([name for name,group in groupby(st.lower().split(' ')) if len(list(group))>=2])
-------------------------------------------------------------------------------
from itertools import groupby

def count_adjacent_pairs(s):
    return sum(next(y) == next(y, 0) for x, y in groupby(s.lower().split()))
-------------------------------------------------------------------------------
def count_adjacent_pairs(st): 
    s, one, two, c = st.lower().split(' '), None, None, 0
    for w in s:
        c += w == one and w != two
        two = one
        one = w
    return c
-------------------------------------------------------------------------------

"""
