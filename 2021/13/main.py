from pprint import pprint

f = open('demo_input.txt','r')
filedata = f.readlines()
f.close()

dotlist = []

def foldbyx(array,foldpoint):
    new_array = []
    for line in array:
        halfa = line[:foldpoint]
        halfb = line[foldpoint:]
        halfb = halfb[::-1]
        print(halfa,halfb)
        for count in range(len(halfa)):
            if halfb[count]=='#':
                halfa[count]='#'
        new_array.append(halfa)
    return new_array

def foldbyy(array,foldpoint):
    new_array = []
    for count in range(foldpoint):
        linea = array[count]
        lineb = array[foldpoint+foldpoint-count]
        for count in range(len(linea)):
            if lineb[count]=='#':
                linea[count]='#'
        new_array.append(linea)
    return new_array

def printdots(array):
    for line in array:
        for char in line:
            print(char,end='')
        print()

def countdots(array):
    count = 0
    for line in array:
        for char in line:
            if char == '.':
                count = count + 1
    return count



maxx=0
maxy=0
dotlist=[]
foldlist=[]
readmode = 'dots'
for line in filedata:
    line = line.strip()
    if line == '':
        pass
    elif line[0].isnumeric():
        x,y = line.split(',')
        x=int(x)
        y=int(y)
        if maxx < x:
            maxx = x
        if maxy < y:
            maxy = y
        dotlist.append([x,y])
    else:
        line = line.strip()
        line = line [11:]
        axis,fold = line.split('=')
        foldlist.append([axis,fold])

dots = [['.' for c in range(maxx+1)] for r in range(maxy+1)]
for x,y in dotlist:
    dots[y][x]='#'

printdots(dots)
for axis,fold in foldlist:
    if axis == 'x':
        dots = foldbyx(dots,int(fold))
    if axis == 'y':
        dots = foldbyy(dots,int(fold))
    printdots(dots)
    print(countdots(dots))
