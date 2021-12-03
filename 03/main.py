

f = open('input.txt','r')
data=f.readlines()
f.close()

#data = ('00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010')
"""
#part 1
bitrow = data[0].strip()
bits = ''
for bit in range(0,len(bitrow)):
    count0 = 0
    count1 = 0
    for row in data:
        row = row.strip() #remove enter from end of line
        if row[bit] == '0':
            count0 = count0 + 1
        if row[bit] == '1':
            count1 = count1 + 1
    if count0 > count1:
        bits = bits + '0'
    else:
        bits = bits + '1'

print(bits)
gamma= int(bits,2)
least = ''
for bit in bits:
    if bit == '0':
        least = least + '1'
    else:
        least = least + '0'
print(least)
epsilon= int(least,2)
print(gamma,epsilon,gamma*epsilon)

"""

#part 2
f = open('input.txt','r')
data=f.readlines()
f.close()

for bit in range(len(data[0])):
    filtered0 = list(filter(lambda row: row[bit] == '0', data))
    filtered1 = list(filter(lambda row: row[bit] == '1', data))
    if len(filtered0) > len(filtered1):
        data=filtered0
    else:
        data=filtered1
    if len(data)==1:
        oxygen=int(data[0],2)
        break

f = open('input.txt','r')
data=f.readlines()
f.close()

for bit in range(len(data[0])):
    filtered0 = list(filter(lambda row: row[bit] == '0', data))
    filtered1 = list(filter(lambda row: row[bit] == '1', data))
    if len(filtered0) > len(filtered1):
        data=filtered1
    else:
        data=filtered0
    if len(data)==1:
        scrubber=int(data[0],2)
        break
print(oxygen*scrubber)
