'''
Poker hands

Problem 54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:

2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

import numpy as np
def read_data():  # read data from Poker Hands text file
   with open('C:\\Users\\Dennis\\OneDrive\\Programming\\Python\Project Euler Problems\\054 - Poker Hands.txt') as f:
      lines = f.readlines()
   t=[]
   for i in lines:
      t.append(i.lstrip('ï»¿').rstrip('\n'))
   return t

def format_data(one_hand):  # process data from one hand
   s=one_hand.replace('A','14').replace('J','11').replace('T','10').replace('Q','12').replace('K','13')
   y=[]
   for i in s.split(' '):
      if len(i)!=3:
         y.append('0'+i)
      else:
         y.append(i)
   val=[]
   suit=[]
   hands=[]#{1:[],2:[]}
   cnt=0
   k=1
   for i in y:
      val.append(i[:2])
      suit.append(i[-1])
      cnt+=1
      if cnt==5 or cnt==10:
         hands.append([sorted(val,reverse=True),suit])
         val=[]
         suit=[]
         k+=1
   return hands  #{1: [['03', '10', '04', '02', '06'], ], 2: [['06', '02', '11', '04', '05'], ['S', 'C', 'H', 'S', 'C']]}

def process_data(data):
   final_hand=[]
   win_1=0
   win_2=0
   tied=0
   for z in data:
      x=format_data(z)
      for p in range(0,2):
         s=x[p][1]   #  ['D', 'S', 'D', 'H', 'H']
         c=x[p][0]   # [ '10', '06', '04','03', '02']
         t=np.unique(c)
         g=['00000']
         for u in t:
            a=np.array(c)
            b=(a==u)
            if len(b[a==u])>0:
               g+=str(len(b[a==u]))
         aa = sorted(c, reverse=True)
         print(aa)
         b = {}
         for i in aa:
            b[i] = aa.count(i)
         v = dict(sorted(b.items(), key=lambda item: item[1], reverse=True))
         tt = ""
         for i in v.items():
            tt += i[0]
         w=(''.join(sorted(g,reverse=True))[ 0:5])
         if w=='11111':
            # print(int(c[0]),int(c[4])+4 )
            if int(c[0])==int(c[4])+4 and len(np.unique(s))==1:
               w='70000'  # straight flush
            elif int(c[0])==int(c[4])+4: 
               w='31400'  # straight
            elif len(np.unique(s))==1:
               w='31500' # flush
            else: w='11111'  #l
         w+=tt
         final_hand.append(w)
      if final_hand[0]>final_hand[1]: 
         win_1+=1
      elif final_hand[0]<final_hand[1]:
         win_2+=1
      else:
         tied+=1
      final_hand=[]
      # print(f'\nwin_1: {win_1}   \nwin_2: {win_2}\nTied: {tied} \n---------------------------------------------------')
   return win_1
         
data=read_data()

print(process_data(data))

'''
Answer:  376

Completed on Mon, 12 Dec 2022, 10:41
'''

'''
GOOD ANSWER

rankvalues = dict((r,i) 
for i,r in enumerate('..23456789TJQKA'))

def poker(hand):
    hand = hand.split()
    
    suits = [s for r,s in hand]
    ranks = sorted([rankvalues[[i][/i]r] for r,s in hand])
    ranks.reverse()
    flush = len(set(suits)) == 1
    straight = (max(ranks)-min(ranks))==4 
                and len(set(ranks))==5

    def kind(n, butnot=None):
        return some(r for r in ranks
                    if ranks.count(r) == n and r != butnot)


    if straight and flush: return 9, ranks
    if kind(4): return 8, kind(4), kind(1)
    if kind(3) and kind(2): return 7, kind(3), kind(2)
    if flush: return 6, ranks
    if straight: return 5, ranks
    if kind(3): return 4, kind(3), ranks
    if kind(2) and kind(2, kind(2)): 
        return 3, kind(2), kind(2, kind(2)), ranks
    if kind(2): return 2, kind(2), ranks
    return 1, ranks

print sum(poker(line[0:14]) > poker(line[15:29])
                 for line in file("poker.txt"))
                 
'''