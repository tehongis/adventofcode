
from pprint import pprint


def stripall(data):
    newdata=[]
    for line in data:
        newdata.append(line.strip())
    return newdata

def count_hor():
    count = 0
    for line in data:
        if "XMAS" in line:
            count=count+1
        if "SAMX" in line:
            count=count+1
    return count

def count_ver():
    count = 0
    for line in rotateddata:
        if "XMAS" in line:
            count=count+1
        if "SAMX" in line:
            count=count+1
    return count

def count_diag():
    count = 0
    for row in range(len(data)-3):
        muhju=[]
        muhju.append(data[row])
        muhju.append(data[row+1])
        muhju.append(data[row+2])
        muhju.append(data[row+3])

        for column in range(len(muhju[0])-3):
            word = muhju[0][column] + muhju[1][column+1] + muhju[2][column+2] + muhju[3][column+3]
            if word=='XMAS':
                count = count + 1
            if word=='SAMX':
                count = count + 1

        for column in range(3,len(muhju[0])):
            word = muhju[0][column] + muhju[1][column-1] + muhju[2][column-2] + muhju[3][column-3]
            if word=='XMAS':
                count = count + 1
            if word=='SAMX':
                count = count + 1

    return count


with open("input.txt", "r") as infile:
    data=infile.readlines()

    data=stripall(data)

    rotateddata=[]
    for column in range(0,len( data[0] ) ):
        newline = ""
        for line in range(0,len(data)):
            newline=newline+(data[line][column])
        rotateddata.append(newline)


result = 0
result = result + count_hor()
result = result + count_ver()
result = result + count_diag()

pprint(result)
