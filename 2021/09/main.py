import pygame
from pygame.locals import *

"""
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.
The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.
Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
"""
colors = {
        "Cadet Blue Crayola":"#96adc8","Mindaro":"#d7ffab","Laser Lemon":"#fcff6c","Tan Crayola":"#d89d6a","Rose Ebony":"#6d454c",
        "Rich Black":"#093a3e","Verdigris":"#3aafb9","Electric Blue":"#64e9ee","Pale Cerulean":"#97c8eb",
        "Maximum Blue":"#5eb1bf","Light Cyan":"#cdedf6","Mandarin":"#ef7b45","Vermilion":"#d84727"
        }

f=open('input.txt','r')
filedata=f.readlines()
f.close()

data = []
for line in filedata:
    line=line.strip()
    integer_line = list(map(int, line))
    data.append(integer_line)

rows=len(data)
row_size=len(data[0])

def check(x,y):

    v=data[y][x]

    if y > 0:
        u=data[y-1][x]
    else:
        u=9
    if y < rows-1:
        d=data[y+1][x]
    else:
        d=9
    if x > 0:
        l=data[y][x-1]
    else:
        l=9
    if x < row_size-1:
        r=data[y][x+1]
    else:
        r=9

    #print(l,u,v,d,r)

    #print(x,y)
    if v<l and v<u and v<d and v<r:
        return True
    else:
        return False

""" 
# Part one
count = 0
for y in range(0,rows):
    for x in range(0,row_size):
        if check(x,y):
            v=data[y][x]
            count = count + ( v + 1 )
            #print('x',end='')
            print(color.BOLD+str(v)+color.END,end='')
        else:
            #print('.',end='')
            v=data[y][x]
            print(v,end='')

    print()
print(count)
"""
# Part two

try:
    pygame.init()
    screen=pygame.display.set_mode((row_size*8,rows*8))
    pixels = pygame.Surface((row_size,rows))
    for y in range(0,rows):
        for x in range(0,row_size):
            v=data[y][x]
            if v == 9:
                pixels.set_at( (x,y) , colors["Pale Cerulean"] )
            else:
                pixels.set_at( (x,y) , colors["Rich Black"] )
    pygame.transform.scale(pixels, (row_size*8,rows*8), screen)
    pygame.display.update()

    RUNNING=True
    while RUNNING:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                RUNNING=False


finally:
    pygame.quit()   

