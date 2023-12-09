from pprint import pprint

import re

#inputdata = ["32T3K 765","T55J5 684","KK677 28","KTJJT 220","QQQJA 483"]

f = open('input.txt','r')
inputdata = f.readlines()
f.close()





fives=[]
fours=[]
fullhouses=[]
threes=[]
twopairs=[]
pairs=[]
highs=[]


def countPairs(hand):
    counts = []
    cardtypes = ''.join(set(hand))
    for card in cardtypes:
        counts.append( hand.count(card) )
    return counts

#Five of a kind, where all five cards have the same label: AAAAA
def checkFive(hand):
    pairs = countPairs(hand)
    if 5 in pairs:
        return True
    return False

#Four of a kind, where four cards have the same label and one card has a different label: AA8AA
def checkFour(hand):
    pairs = countPairs(hand)
    if 4 in pairs:
        return True
    return False

#Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
def checkFullHouse(hand):
    if checkThree(hand) and checkPair(hand):
        return True
    return False

#Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
def checkThree(hand):
    pairs = countPairs(hand)
    if 3 in pairs:
        return True
    return False

#Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
def checkTwoPairs(hand):
    pairs = countPairs(hand)
    if pairs.count(2) == 2:
        return True
    return False

#One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
def checkPair(hand):
    pairs = countPairs(hand)
    if 2 in pairs:
        return True
    return False

#High card, where all cards' labels are distinct: 23456
def checkHigh(hand):
    return True
    



for line in inputdata:
    line = line.strip()
    hand,bet = line.split(' ')
    bet = int(bet)
    #hand = sorted(hand)
    if checkFive(hand):
        #print("Five found:" + hand)
        fives.append( (hand,bet) )
        continue
    if checkFour(hand):
        #print("Four found:" + hand)
        fours.append( (hand,bet) )
        continue        
    if checkFullHouse(hand):
        #print("Fullhouse found:" + hand)
        fullhouses.append( (hand,bet) )
        continue        
    if checkThree(hand):
        #print("Three found:" + hand)
        threes.append( (hand,bet) )
        continue        
    if checkTwoPairs(hand):
        #print("Two pairs found:" + hand)
        twopairs.append( (hand,bet) )
        continue        
    if checkPair(hand):
        #print("Pair found:" + hand)
        pairs.append( (hand,bet) )
        continue        
    if checkHigh(hand):
        #print("Highcard found:" + hand)
        highs.append( (hand,bet) )
        continue        
#    games.append( ( hand,bet ) )

def cardSort(hands):
    values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

    getValue = lambda cards: values[cards[:-1]]

    def splitHand(hand):
        cards,bet = hand
        return cards

    return sorted(hands,key=getValue)

#fives.sort()
#fours.sort()

#pprint(fives)
#pprint(fours)
pprint(cardSort(fullhouses))
#pprint(fullhouses)
#pprint(threes)
#pprint(twopairs)
#pprint(pairs)
#pprint(highs)

#games.sort(reverse=True)
#games.sort()
#for hand,bet in games:
#    print( hand,bet  )
