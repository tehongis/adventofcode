

file = open('input.txt','r')
data = file.readlines()
file.close()

bags = []

for count,line in enumerate(data, start=0):
    line = line.rstrip()
    bag,content = line.split(' contain ')
#    print(content)
    if bag not in bags:
        bags.append((bag,content))
        for inbag in content.split(','):
            inbag = inbag.lstrip()
            if 'gold' in inbag:
                print(inbag)

#        print('Added ',bag)
    else:
        print("Already listed ",bag)

print(count)
