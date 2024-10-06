
'''
Problem #: 18

https://projecteuler.net/problem=18

Difficulty: 5%

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

Answer:  1074
Completed on Mon, 17 May 2021, 16:30

-----------------------------------------------------
3 
7 4
2 4 6
8 5 9 3

	2 + 8 = 10
	2 + 5 = 7
    10 is greater than 7 and 2 is replaced with 10.

   3
  7 4
 2 4 6  
8 5 9 3

Let’s say you’re on the penultimate level 2 4 6 and you have to iterate over it.

From 2, you can go to either 8 or 5, so 8 is better (maximize you result by 3) so you calculate the first sum 8 + 2 = 10

From 4, you can go to either 5 or 9, so 9 is better (maximize you result by 4) so you calculate the second sum 9 + 4 = 13

From 6, you can go to either 9 or 3, so 9 is better again (maximize you result by 6) so you calculate the third sum 9 + 6 = 15

This is the end of first iteration and you got the line of sums 10 13 15. 

      3
   7    4
10   13    15 

Keep going this way…

         3
     20    19
…and you finally arrive at 23 as the answer.

https://pythonandr.com/2015/09/05/maximum-path-sum-dynamic-programming-algorithm/

---------------------------------------------------

fi = open('18.dat', 'r')
Tri=[]
for line in fi:
    Tri.append( map( int, line.split() ) )

ms=0 # maxsum
def sub( r, c, s ): # row, column, sum
    r+=1
    if r==len(Tri):
        global ms
        if s>ms: 
            ms=s
        return
    for i in [0,1]: 
        sub( r, c+i, s+Tri[r][c+i] )

sub( 0, 0, Tri[0][0] )
print ms
----------------------------------------------------------
data = [[int(n) for n in s.split()] for s in open('prob18.txt').readlines()]
max_sum = 0
def find_sums(r=0,c=0,total=0):
	global max_sum
	total += data[r][c]
	if r == len(data) - 1:
		if total > max_sum:
			max_sum = total
		return
	else:
		find_sums(r+1,c,total)
		find_sums(r+1,c+1,total)
find_sums()
print max_sum
-----------------------------------------------------------------
temp = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

t = map(lambda x: map(int, x.split()), temp.split('\n'))

def maxsum(sum, line):
    a = map(lambda x: x[0]+x[1], zip(sum, line))
    b = map(lambda x: x[0]+x[1], zip(sum[1:], line))
    return map(max, zip(a, b))

print reduce(maxsum, t[::-1])

'''

def prt(*args):
    print() 
    print(*args)

def max_path_sum(triangle):

    n = len(triangle)
    p = [0] * n
    for i in range(n):
        t = p.copy()
        t[0] = p[0] + triangle[i][0] 
        for j in range(1, i):
            t[j] = max(p[j - 1], p[j]) + triangle[i][j]
        t[i] = p[i - 1] + triangle[i][i]  
        p = t
        # prt(triangle[i][0],p[0],p)

    return max(p) 

triangle = [
                                    [75],
                                  [95, 64],
                                [17, 47, 82],
                              [18, 35, 87, 10],
                            [20,  4, 82, 47, 65],
                          [19,  1, 23, 75,  3, 34],
                        [88,  2, 77, 73,  7, 63, 67],
                      [99, 65,  4, 28,  6, 16, 70, 92],
                    [41, 41, 26, 56, 83, 40, 80, 70, 33],
                  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
              [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
          [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
           ]

prt('Answer: ',max_path_sum(triangle))


