f = open('demo_input.txt','r')
filedata=f.readlines()
f.close()


class cave:

    def __init__(self,name):
        self.name = name
        self.small = name.islower()
        self.visited = False
        self.links = []


caves = []

def caveindex(name):
    for index, cavelook in enumerate(caves):
        if cavelook.name == name:
            return index
    return False

for line in filedata:
    line=line.strip()
    cavefrom,caveto = line.split('-')

    fromindex = caveindex(cavefrom)
    toindex = caveindex(caveto)

    if not fromindex:
        caves.append(cave(cavefrom))
    else:
        if caveto not in caves[fromindex].links:
            cavefrom.links.append(cave(caveto))

    if caveto not in caves:
        caves.append(cave(caveto))


for cave in caves:
    print(cave.name,cave.small,cave.visited,cave.links)
