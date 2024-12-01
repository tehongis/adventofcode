from pprint import pprint

with open("input.txt", "r") as infile:
    data=infile.readlines()

lista = []
listb = []

for row in data:
    row = row.strip()
    a,b=row.split('   ')
    lista.append(a)
    listb.append(b)

lista.sort()
listb.sort()

result = 0
for idx,a in enumerate(lista):
    a=int(a)
    b=int(listb[idx])
    diff = abs(a-b)
    result = result + diff
    pprint([idx,a,b,diff,result])
