'''^Cubic permutations

Problem 62

Started: 13 March 2023

Answer:  Answer:  127035954683

Completed on Thu, 16 Mar 2023, 20:30



The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''


def is_cubic_permute(n1, n2):
    s1 = ''.join(sorted(str(n1)))
    s2 = ''.join(sorted(str(n2)))
    return s1 == s2

d=[]
for i in range(5000,9000):
    d.append(i**3)

for i in range(0,len(d)):
    e=[d[i]]
    for j in range(i+1,len(d)):
        if is_cubic_permute(d[i],d[j]):
            e.append(d[j])
    if len(e)==5:
        print(f'The answer is = {e[0]}')
#* bob us here
