from pprint import pprint
import pygame
from pygame.locals import *


SC_SIZE = (1280,800)
BG_COLOR = (0,0,0)
FG_COLOR = (255,255,255)

f = open('input.txt')
filedata=f.readlines()
f.close()


image = []
for row in filedata[2:]:
    row = row.strip()
    image.append(row)

enhancer = filedata[0].strip()

def image2surf(image):
    rows = len(image)
    rowsize = len(image[0])
    SURF_SIZE = (rowsize,rows)
    surf = pygame.Surface(SURF_SIZE)
    for y,row in enumerate(image):
        for x,pixel in enumerate(row):
            if pixel == '#':
                surf.set_at((x,y),FG_COLOR)
    return surf

def enhancepixel(surf,coords):
    mini_surf = pygame.Surface( (3,3) )
    mini_surf.blit(surf, (0,0) , (coords[0],coords[1],3,3) )

    bits = ''
    for y in range(0,3):
        for x in range(0,3):
            if mini_surf.get_at( (x,y) ) == FG_COLOR:
                bits += '1'
            else:
                bits += '0'
    index = int(bits,2)
    if enhancer[index] == '#':
        return FG_COLOR
    else:
        return BG_COLOR

def enhanceimage(surf):
    surfsize = ( surf.get_height() + 2   , surf.get_width() + 2 )
    new_surf = pygame.Surface(surfsize)
    for y in range(surf.get_height() ):
        for x in range(surf.get_width() ):
            new_surf.set_at( (x+1,y+1), enhancepixel(surf,(x,y)) )
    return new_surf


try:
    pygame.init()
    screen= pygame.display.set_mode(SC_SIZE)
    clock=pygame.time.Clock()

    surf = image2surf(image)


    RUNNING = True
    while(RUNNING):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                RUNNING=False

        screen.fill(BG_COLOR)

        double_surf = pygame.transform.scale(surf,( surf.get_width() * 4, surf.get_height() * 4 ))
        locx = double_surf.get_width()/2
        locy = double_surf.get_height()/2
        screen.blit(double_surf, (SC_SIZE[0]/2-locx - 250, SC_SIZE[1]/2-locx) )

        new_surf = enhanceimage(surf)
        double_surf = pygame.transform.scale(new_surf,( new_surf.get_width() * 4, new_surf.get_height() * 4 ))
        locx = double_surf.get_width()/2
        locy = double_surf.get_height()/2
        screen.blit(double_surf, (SC_SIZE[0]/2-locx + 250, SC_SIZE[1]/2-locx) )

        surf = new_surf

        pygame.display.update()
        clock.tick(30)

finally:
    pygame.quit()