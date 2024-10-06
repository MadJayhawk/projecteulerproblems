'''

Problem #: 39

https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximized?

Answer:  840
Completed on Mon, 20 Mar 2023, 20:46
'''

f={}
d=[]
i = 3
while i<=45:
    if i%2 !=0:
        x=i
        y=int((i*i-1)/2) 
        z=int((i*i+1)/2)
        p=int(x+y+z)
    else:
        x=i
        y=int((i*i/4)-1)  
        z=int((i*i/4)+1)  
        p=int(i+y+z)  
        if sorted([x,y,z]) not in d and p<=1000:
            d.append(sorted([x,y,z]))    
    i+=1

for i in d:
    p=1
    k=2
    while p<= 1000: 
            a=k*i[0]
            b=k*i[1]
            c=k*i[2]
            p=a+b+c
            if sorted([a,b,c]) not in d and p<=1000:
                d.append(sorted([a,b,c]))

            k+=1 

for i in d:
    k=sum(i)
    if k in f:
        f[k]+=1
    else:
        f[k]=1
print(f'p = {max(f, key=f.get)}')

'''
from collections import Counter
me = []
for a in range(1,1001):
    for b in range(1,1001):
        c = (a*a+b*b)**0.5
        p = a+b+c
        if p<=1000:
            me.append(p)
c = Counter(me)

print(c.most_common(1))
------------------------------------------------
max_count=0
for p in range(3,1001):
    count=0
    for c in range(int(p/3),int(p/2)):
        for b in range(int(p/3),c+1):
            a=p-b-c
            if (a**2)+(b**2)==(c**2):
                count+=1
    if count>max_count:
        max_count=count
        answer=p
print(answer)
'''