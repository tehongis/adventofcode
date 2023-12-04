from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

results = []

total_wins = 0
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


    outline = f"{card} : {winners} : {numbers}"
    print(outline)
    wins = 0
    for winner in winners:
        for number in numbers:
            if number == winner:
                if wins == 0:
                    wins=1
                else:
                    wins = wins * 2
    print(wins)
    results.append(wins)
    total_wins = total_wins + wins

print(total_wins)

