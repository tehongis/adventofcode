from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()


seeds = []
soilmap = []
fertilizermap = []
watermap = []
lightmap = []
temperaturemap = []
humiditymap = []
locationmap = []


mode = ''
for line in inputdata:
    line = line.strip()
    #print(line)

    if 'seeds:' in line:
        temp = line.split(':')[1]
        temp = temp.strip()
        seeds_string = temp.split(' ')
        for seed in seeds_string:
            seeds.append(seed)
        continue

    match mode:
        case 'seed-to-soil map':
            x,y,z = line.split(' ')
            soilmap.append( (x,y,z) )

        case 'soil-to-fertilizer map':
            x,y,z = line.split(' ')
            fertilizermap.append( (x,y,z) )

        case 'fertilizer-to-water map':
            x,y,z = line.split(' ')
            watermap.append( (x,y,z) )

        case 'water-to-light map':
            x,y,z = line.split(' ')
            lightmap.append( (x,y,z) )

        case 'light-to-temperature map':
            x,y,z = line.split(' ')
            temperaturemap.append( (x,y,z) )

        case 'temperature-to-humidity map':
            x,y,z = line.split(' ')
            humiditymap.append( (x,y,z) )

        case 'humidity-to-location map':
            x,y,z = line.split(' ')
            locationmap.append( (x,y,z) )

    if line == '':
        mode = ''

    if ':' in line:
        mode,temp = line.split(':')
        print(mode)

pprint(seeds)
pprint(soilmap)
pprint(fertilizermap)
pprint(watermap)
pprint(lightmap)
pprint(temperaturemap)
pprint(humiditymap)
pprint(locationmap)
