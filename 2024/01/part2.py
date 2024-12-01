from pprint import pprint

with open("input.txt", "r") as infile:
    data=infile.readlines()

lista = []
listb = []

for row in data:
    row = row.strip()
    a,b=row.split('   ')
    lista.append(int(a))
    listb.append(int(b))

lista.sort()
listb.sort()

result = 0
for idx,a in enumerate(lista):
    count = listb.count(a)
    result = result + a*count 

print(result)