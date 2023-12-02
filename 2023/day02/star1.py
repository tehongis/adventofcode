from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

RED_MAX = 12;
GREEN_MAX = 13;
BLUE_MAX = 14;

#370 too low

def parseSets(sets):
    for set in sets:
        if not parseSet(set):
            return True
    return False


def parseSet(set):
    cubes = set.split(',')
    for cube in cubes:
        cube = cube.lstrip()
        number,color=cube.split(' ')
        number=int(number)
        match color:
            case 'red':
                if number > RED_MAX:
                    return False
            case 'green':
                if number > GREEN_MAX:
                    return False
            case 'blue':
                if number > BLUE_MAX:
                    return False
    return True


# Game 32:  2 blue, 14 red, 13 green;
#           11 red, 3 green, 1 blue;
#           9 red, 2 blue, 2 green;
#           5 blue, 3 red, 2 green;
#           4 blue, 8 green, 6 red;
#           12 red, 4 green, 5 blue
idcount = 0
for line in inputdata:
    line=line.strip()

    game,results = line.split(':')
    game=int(game.split(' ')[1])

    sets = results.split(';')
    if parseSets(sets):
        out = f"Game {game} failed: {sets}"
    else:
        idcount= idcount + game
        out = f"Game {game} success: {sets}"
    print(out)

print(idcount)





#print(good_games)

