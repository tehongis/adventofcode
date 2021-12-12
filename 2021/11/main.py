import os
import time
from pprint import pprint
f = open('demo_input.txt','r')
filedata=f.read()
f.close()

data = filedata.split()
data=[list(map(int, i)) for i in data]

def add_one(array):
    new_array = []
    for y,line in enumerate(array):
        new_line=[]
        for x,number in enumerate(line):
            new_line.append( array[y][x] + 1 )
        new_array.append(new_line)
    return new_array

def add_list(array,list):
    new_array = []
    for x,y in list:

    for y,line in enumerate(array):
        new_line=[]
        for x,number in enumerate(line):
            new_line.append( array[y][x] + 1 )
        new_array.append(new_line)
    return new_array

def get_add_list(array):
    add_list = []
    for y,line in enumerate(array):
        for x,number in enumerate(line):
            if number >= 9:
                add_list.append([x,y])

                add_list.append([x-1,y-1])
                add_list.append([x,y-1])
                add_list.append([x+1,y-1])

                add_list.append([x-1,y])
                add_list.append([x+1,y])

                add_list.append([x-1,y+1])
                add_list.append([x,y+1])
                add_list.append([x+1,y+1])

                number = 0
    return add_list

#for line in data:
#    print(line)

pprint(data)
add_list = get_add_list(data)

data = add_one(data)
