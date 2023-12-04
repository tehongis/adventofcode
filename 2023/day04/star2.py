from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

results = []


def getWins(card):
    return results[card]

for row_number,line in enumerate(inputdata):
    line = line.strip()
    card,rest = line.split(':')
    winners,numbers = rest.split('|')
    
    winners=winners.strip()
    numbers=numbers.strip()

    winners=winners.replace('  ',' ')
    numbers=numbers.replace('  ',' ')

    winners=winners.split(' ')
    numbers=numbers.split(' ')

    wins = 0
    for winner in winners:
        for number in numbers:
            if number == winner:
                wins = wins + 1
    results.append(wins)

total_wins = 0
for index,result in enumerate(results):
    total_wins = total_wins + result
    print(index+1, result)

print(total_wins)
