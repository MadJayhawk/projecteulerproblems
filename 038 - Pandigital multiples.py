'''

Problem #: 38

https://projecteuler.net/problem=38

Difficulty: 5%

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

answer = 9322718654 
'''

# for n in range(2, 10):
#     for i in range(1, 10**(9 // n)):
#         s = "".join(str(i * j) for j in range(1, n + 1))
#         if "".join(sorted(s)) == "123456789":
#             ans = max(s, ans)
# print(ans) \
# e=[]
# for a in range(900000000,1000000000):   
#     d=[]
#     i=1
#     while i<=9:
#         b=list(str(a * i))   
#         for j in b:           
#             if j in d or j=='0': 
#                 if len(d)==9:
#                     c=int(''.join(d)) 
#                     if c not in e:
#                         e.append(c)   
#                 d=[]
#                 i=10
#                 break 
#             else: 
#                 d.append(j)   
#         i+=1     
#     # print(a,d,e)
#         # print(''.join(d),len(d))
    
# print(e,'\n','\n',max(e))
# print()

# for x in range(9000, 10000):
#   strx = str(x)
#   otherstrx = str(x*2)
#   comb = strx+otherstrx
#   if comb.count('1') == 1 and comb.count('2') == 1 and comb.count('3') == 1 and comb.count('4') == 1 and comb.count('5') == 1 and comb.count('6') == 1 and comb.count('7') == 1 and comb.count('8') == 1 and comb.count('9') == 1:
#     print(comb)

mayor = 0

for i in range(1, 10000):
    conc = str(i*1)
    for j in range(2, 6):
        conc += str(i*j)
        if "".join(sorted(list(conc))) == "123456789" and int(conc) > mayor: mayor = int(conc)
        
print(mayor)