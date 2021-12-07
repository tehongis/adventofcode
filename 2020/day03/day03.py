

file = open('day03-input.txt','r')
data = file.readlines()
file.close()

nr_lines = len(data)

tree_count = 0

x_location = 0

for count,line in enumerate(data, start=0):
    line = line.rstrip()
    print(line,x_location,line[x_location])
    if(line[x_location] == '#' ):
        tree_count = tree_count + 1
    x_location = (x_location + 3) % 31
    
print(nr_lines,tree_count)
"""
    rule,password = line.split(':')
    password = password.strip(' ')
    numbers,letter = rule.split(' ')
    low,hi = numbers.split('-')
    low = int(low) - 1
    hi = int(hi) - 1
    print(rule,password,password[low],password[hi])
90 * 244 * 97 * 92 * 48
"""
