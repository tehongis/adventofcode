

f=open('input.txt','r')
filedata=f.readlines()
f.close()




data = []
for line in filedata:
    line=line.strip()
    integer_line = list(map(int, line))
    data.append(integer_line)

rows=len(data)
rowsize=len(data[0])


def check(x,y):
    #print(x,y)
    v=data[y][x]
    if y > 0 and y < rows and x > 0 and x < rowsize:
        if v<data[y][x-1] and v<data[y][x]+1 and v<data[y-1][x] and v<data[y+1][x]:
            return True
    return False

count = 0
for y in range(0,rows-1):
    for x in range(0,rowsize):
        if check(x,y):
            v=data[y][x] + 1
            count = count + v
            print('x',end='')
        else:
            print('.',end='')
    print()
print(count)
