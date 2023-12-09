from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

results = []


def getWins(card):
    value = 0
    for count in range(card,card+results[card]):
        print("\t"+str(count),end="")
        temp = results[count]
        print( "\t\t:" + str(temp) )
        value = value + temp
    return value

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

cumulative = []
for index,result in enumerate(results):
    print(result)
    value = getWins(index)
    print("\t\t"+str(value))
    cumulative.append( value )
    if index == 5:
        break


#for index,result in enumerate(results):
#    print(results[index],cumulative[index])
