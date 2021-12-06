import math
from pprint import pprint

DAYS = 256

f = open('input.txt','r')
filedata = f.readlines()
f.close()

parvi = [0,0,0,0,0,0,0,0,0]

data = filedata[0].strip().split(',')
for number in data:
    number = int(number)
    parvi[number] += 1 




for day in range(DAYS):

    add = parvi[0]
    parvi[0] = parvi[1]
    parvi[1] = parvi[2]
    parvi[2] = parvi[3]
    parvi[3] = parvi[4]
    parvi[4] = parvi[5]
    parvi[5] = parvi[6]
    parvi[6] = parvi[7] + add
    parvi[7] = parvi[8]
    parvi[8] = add

    total = 0
    for fishcount in parvi:
        total = total +fishcount
    print(day+1,total)
