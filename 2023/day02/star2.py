from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()


def parseSets(sets):
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in sets:
        red,green,blue = parseSet(set)
        if red > max_red:
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue
    return max_red,max_green,max_blue


def parseSet(set):
    red = 0
    green = 0
    blue = 0
    cubes = set.split(',')
    for cube in cubes:
        cube = cube.lstrip()
        number,color=cube.split(' ')
        number=int(number)
        match color:
            case 'red':
                red = number
            case 'green':
                green = number
            case 'blue':
                blue = number
    return red,green,blue


# Game 32:  2 blue, 14 red, 13 green;
#           11 red, 3 green, 1 blue;
#           9 red, 2 blue, 2 green;
#           5 blue, 3 red, 2 green;
#           4 blue, 8 green, 6 red;
#           12 red, 4 green, 5 blue
total_power = 0
for line in inputdata:
    line=line.strip()

    game,results = line.split(':')
    game=int(game.split(' ')[1])

    sets = results.split(';')
    r,g,b = parseSets(sets)
    power = r*g*b
    out = f"Game {game}: {r}-{g}-{b} -> {power} : {sets} "
    total_power=total_power + power
    print(out)
print(total_power)