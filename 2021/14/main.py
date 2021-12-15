
f = open('input.txt','r')
filedata = f.readlines()
f.close()


rules=[]
for count,line in enumerate(filedata):
    line = line.strip()
    if count == 0:
        polymer = line
    else:
        if line=='':
            pass
        else:
            what,add = line.split(' -> ')
            rules.append([what,add])


for kerta in range(1,40+1):
    print(kerta)
    result = polymer[0]
    for count in range(len(polymer)-1):
        pair=polymer[count]+polymer[count+1]
        for what,add in rules:
            if pair == what:
                result = result+add+pair[1]
    polymer = result

result = sorted(result)
sizes=[]
for char in list(set(result)):
    sizes.append(result.count(char))

large = max(sizes)
small = min(sizes)
print(large-small)