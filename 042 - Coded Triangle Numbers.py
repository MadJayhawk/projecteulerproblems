'''
Problem #: 42

https://projecteuler.net/problem=42

Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
with open ("C:\\Users\\Dennis\\OneDrive\\Programming\\Python\Project Euler Problems\\CodeLibrary\\ss.txt", "r") as fileHandler:
    # Read each line in loop
    for line in fileHandler:
        # As each line (except last one) will contain new line character, so strip that

        a=line.strip() 
print(a)
print()
f=[]
for i in range(200):
    f.append(int((i*(i+1))/2))
# print(f)
s=[]
t=[]
cnt=0
for word in a:
    if word==',':
        if sum(s) in f:
            cnt+=1
        t.append(sum(s))
        s=[]
    else:
        if word!='"':
            s.append(ord(word)-64)
print(cnt)

'''
from math import sqrt; print("The total of triangular word is :", sum([ ((-1+sqrt(8*(sum([ (ord(letter)-ord('A')+1) for letter in word ]))+1))/2).is_integer() for word in open("p042_words.txt").read().replace("\"", "").split(',') ]))
----------------------------------------------------------------
num=[]
trinum=0
for i in range(1,20):
    num.append(i*(i+1)//2)
alp=['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str=list(words.txt)
for j in str:
    sum=0
    for k in list(j):
        sum+=alp.index(k)
    if sum in num:
        trinum+=1
print(trinum)
'''
