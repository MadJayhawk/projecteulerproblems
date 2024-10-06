'''
Powerful digit counts

Problem 63

Started: 16 March 2023  2145

Answer:  Answer:  49

Completed on   17 March 2023  1042

The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?'''

import math
cnt=0
for i in range(1,50):
    for j in range(1,10):
        if math.floor(math.log10(j**i)) + 1 ==i:
            cnt+=1
            # print (j,i,j**i,cnt)
print(f'answer is {cnt}')