from pprint import pprint

f = open('demo_input.txt','r')
filedata = f.readlines()
f.close()

dotlist = []

maxx=0
maxy=0
for line in filedata:
    line = line.strip()
    if line == '':
        break
    x,y = line.split(',')
    x=int(x)
    y=int(y)

    if x > maxx:
        maxx=x
    if y > maxy:
        maxy=y
    dotlist.append([x,y])

print(maxx,maxy)
dots = [['.' for c in range(15)] for r in range(15)]
for x,y in dotlist:
    dots[y][x]='#'

for line in dots:
    for char in line:
        print(char,end='')
    print()
