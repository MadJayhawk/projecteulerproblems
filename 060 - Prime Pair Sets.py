'''

Prime pair sets

Problem 60

Started: 25 Dec 2022, 16:08


Answer:  26033   [13, 5197, 5701, 6733, 8389]

Completed on Tue, 24 Jan 2023, 14:42 adapted from 
https://radiusofcircle.blogspot.com/2016/10/problem-60-project-euler-solution-with.html  Initially tried using combinations of primes without success.  Never could determine reason why my code did not work.  Logically it should have.  


The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''
import sympy
import csv

def write_csv(rt):  # write primes to a CSV file

    cc= list(map(int,sympy.primerange(0,rt)))
    cc=[cc]
    with open('C:\\Users\\Dennis\\OneDrive\\Programming\\Python\\Project Euler Problems\\comb_primes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cc)
        
def write_csv():  # read primes from a CSV file
    x=[]
    with open('C:\\Users\\Dennis\\OneDrive\\Programming\\Python\\Project Euler Problems\\comb_primes.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            x.append(row)
    prmes=x[0]       # list of primes from comb_primes.cvs file
    prmes.remove('2')
    prmes.remove('5')
    return prmes

def comb(a,b):
    if sympy.isprime(int(a+b)) and sympy.isprime(int(b+a)):
        return True
    return False

def calc_prime_pairs(p):
    primes=p
    for i in primes[0:1800]:
        for j in primes[0:1800]:
            if j < i:
                continue
            if comb(i,j):
                # print(i,j)
                for k in primes[0:1800]:
                    if k < j:
                        continue
                    if comb(i,k) and comb(j,k): 
                        # print(i,j,k)
                        for l in primes[0:1800]:
                            if l < k:
                                continue
                            if comb(i,l) and comb(j,l)and comb(k,l):
                                # print(i,j,k,l)
                                for m in primes[0:1800]:
                                    if m < l:
                                        continue
                                    if comb(i,m) and comb(j,m) and comb(k,m) and comb(l,m):
                                        print(i,j,k,l,m)
                                        rr=list(map(int,[i,j,k,l,m]))
    return sum(rr)
read_csv()
pr=write_csv()
answer=calc_prime_pairs(pr)
print(f'answer:  {sum(ans)}')