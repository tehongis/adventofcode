import math
from pprint import pprint

f=open('input.txt','r')
data=f.read()
f.close()

data=data.strip()
data = data.split(',')
data = map(int, data)
data = list(data) 
data.sort()

minimum = min(data)
maximum = max(data)

matkat = []
for count in range(minimum,maximum):
	matkatotal = 0
	for number in data:
		difference = abs(count-number)
		#matkatotal = matkatotal + difference # part 1 calculation
		for difcount in range(1,difference+1):
			matkatotal = matkatotal + difcount # part 2 calculation
	matkat.append(matkatotal)

smallest = min(matkat)
print(matkat.index(smallest),smallest)

