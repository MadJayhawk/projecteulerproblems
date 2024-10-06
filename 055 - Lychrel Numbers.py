'''
Lychrel Numbers

Problem 55

Started:  12-13-22

https://datagenetics.com/blog/october12015/index.html

    If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

    Not all numbers produce palindromes so quickly. For example,

    349 + 943 = 1292,
    1292 + 2921 = 4213
    4213 + 3124 = 7337

    That is, 349 took three iterations to arrive at a palindrome.

    Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

    Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

    How many Lychrel numbers are there below ten-thousand?

'''
def candidate_check(s):         # s = 275                     |  s = 113
    b=str(s)                  # b = 275                     |  b = 113
    a=int(b[::-1])+s          # 572 + 275 = 847             |  311 + 113 = 424
    p=str(a)[::-1] == str(a)  # 748 == 847  False           |  424 == 424  True
    return a,p                # (847, False)  or  (424, True)


l_num=0
for n in range(1,10001):
    candidate,is_ly_num = candidate_check(n)
    no_of_iterations = 0
    while is_ly_num == False and no_of_iterations < 50:
        candidate,is_ly_num = candidate_check(candidate)
        no_of_iterations += 1
    if not is_ly_num:
        l_num += 1
print(f'The answer is {l_num}')