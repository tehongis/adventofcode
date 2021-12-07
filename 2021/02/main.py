
f = open('input.txt','r')
data = f.readlines()
f.close()

"""
position = 0
depth = 0
for row in data:
    row = row.strip()
    command,value = row.split(' ')
    if command == 'forward':
        position = position + int(value)
    if command == 'down':
        depth = depth + int(value)
    if command == 'up':
        depth = depth - int(value)
    print(position,depth)

print(position*depth)
"""

count = 0
position = 0
depth = 0
aim = 0
for row in data:
    row = row.strip()
    command,value = row.split(' ')
    value = int(value)
    if command == 'down':
        aim = aim + value
    if command == 'up':
        aim = aim - value
    if command == 'forward':
        position = position + value
        depth = depth + ( aim * value )
    print(row,position,aim,depth)

print(position*depth)

