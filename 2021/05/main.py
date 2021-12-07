import math
from pprint import pprint

def parsedata():
    f = open('input.txt','r')
    filedata = f.readlines()
    f.close()
    cleaned_data = []
    for row in filedata:
        cleaned_data.append(row.strip())
    return cleaned_data


data = parsedata()

def drawline(map,row):
    start,end = row.split(' -> ')
    x1,y1=start.split(',')
    x2,y2=end.split(',')
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)

    if x1==x2:
        if y1 < y2:
            for y in range(y1,y2+1):
                map[x1][y]=map[x1][y]+1
        else:
            for y in range(y2,y1+1):
                map[x1][y]=map[x1][y]+1

    elif y1 == y2:
        if x1 < x2:
            for x in range(x1,x2+1):
                map[x][y1]=map[x][y1]+1
        else:
            for x in range(x2,x1+1):
                map[x][y1]=map[x][y1]+1

    elif x1 <= x2:
        y=y1
        if y1 < y2:
            for x in range(x1,x2+1):
                map[x][y]=map[x][y]+1
                y=y+1
        else:
            for x in range(x1,x2+1):
                map[x][y]=map[x][y]+1
                y=y-1

    elif x2 <= x1:
        y=y2
        if y1 < y2:
            for x in range(x2,x1+1):
                map[x][y]=map[x][y]+1
                y=y-1
        else:
            for x in range(x2,x1+1):
                map[x][y]=map[x][y]+1
                y=y+1


def printmap(map):
    map = list(zip(*map[::-1]))
    for row in map:
        for number in list(reversed(row)):
            if number == 0:
                print('.',end='')
            else:
                print(number,end='')
        print()

map = []
for y in range(0,1000):
    row = []
    for x in range(0,1000):
        row.append(0)
    map.append(row)

for row in data:  
    drawline(map,row)

count = 0
for row in map:
    for number in row:
        if number >=2:
            count = count + 1
#printmap(map)
print(count)
