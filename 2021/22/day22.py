import numpy
from pprint import pprint

f=open('input.txt')
data=f.readlines()
f.close()

core = numpy.zeros((15,15,15))

def handlearea(state,area):
    if state == 'on':
        state = 1
    else:
        state = 0
    xrange,yrange,zrange=area.split(',')
    xrange=xrange[2:].split('..')
    yrange=yrange[2:].split('..')
    zrange=zrange[2:].split('..')
    for z in range( int(zrange[0]) , int(zrange[1])+1 ):
        for y in range( int(yrange[0]) , int(yrange[1])+1 ):
            for x in range( int(xrange[0]) , int(xrange[1])+1 ):
                core[z][y][x] = state


for line in data:
    line=line.strip()
    state,area = line.split(' ')
    
    handlearea(state,area)

count = numpy.count_nonzero(core == 1)
pprint(count)
