
#https://adventofcode.com/2021/day/1

f = open('input.txt','r')
data = f.readlines()
f.close()

"""
#First part
count = 0
oldvalue =  int(data[0].strip())

for value in data:
    value = int(value.strip())
    if value > oldvalue:
        count = count + 1
        info='+'
    else:
        info=' '
    oldvalue=value
    print(value,info,count)

print(count)
"""

#Second part

def slide(array,value):
    array[0] = array[1]
    array[1] = array[2]
    array[2] = value
    return array

def sum(array):
    return array[0] + array[1] + array[2]

arrayA = [ 0,0,0 ]
arrayB = [ 0,0,0 ]

initcount = 0
count = 0
for value in data:
    value = int(value.strip())
    #print(value)
    arrayA = slide(arrayA,value)
    if initcount < 3:
        initcount = initcount + 1
    else:
        current = sum(arrayA)
        previous = sum(arrayB)
        if current > previous:
            count = count + 1
        print(arrayB, arrayA, previous , current, count )
        #break
    #print(arrayA,arrayB)
    arrayB = []
    for item in arrayA:
        arrayB.append(item)
