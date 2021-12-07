

file = open('input.txt','r')
data = file.readlines()
file.close()

def look_bag(bag):
    for line in data:
        line = line.rstrip()
        line_bag,contents = line.split(' contain ')
        line_bag = line_bag.rstrip('s')
        if line_bag == bag:
            return contents

for count,line in enumerate(data, start=0):
    line = line.rstrip()
    bag,contents = line.split(' contain ')
    bag = bag.rstrip('s')
    print(bag)
    for in_bag in contents.split(','):
        in_bag = in_bag.lstrip()
        if in_bag == 'no other bags.':
            continue
        count = int(in_bag[0])
        in_bag = in_bag[2:]
        in_bag = in_bag.rstrip('.')
        in_bag = in_bag.rstrip('s')
        print("\t" + str(count) + " " + in_bag+ " -> " + str(look_bag(in_bag)))
        #print( bag, look_bag(bag) )
#    break

print(count)
