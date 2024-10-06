'''

XOR decryption

Problem 59

Started: 17 Dec 2022 3:06pm


Answer:   129448
Completed on Sun, 25 Dec 2022, 21:38


Each character on a computer is assigned a unique code and the preferred standard is ASCII (
). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''

import csv
with open("C:\\Users\\Dennis\\OneDrive\\Programming\\Python\Project Euler Problems\\059 - p059_cipher.csv", 'rt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        b=','.join(row)
message=list(map(int,b.split(','))) 

t=['e','x','p']*len(message)//3  # there are 1,455 characters in p059_cipher.cvs  ['e','x','p','e','x','p','e','x','p','e','x','p', etc]
d=[]
e=0
j=0
while j<len(message): 
    for i in t:
        m=chr(ord(i)^message[j])
        print(j,i,ord(i),message[j],m)
        d.append(m)
        e+=ord(m)
        j+=1
print(''.join(d))
print(f'answer is: {e}')

# answer is:  129448

#  text of message

#An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
