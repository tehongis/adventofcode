from pprint import pprint
import numpy as np

times = [34, 90, 89, 86]
distances = [204, 1713, 1210, 1780]
#times = [7, 15, 30]
#distances = [9, 40, 200]


def calcVariations(max_time,target_distance):
    ways = 0
    for count in range(0,max_time):
        speed = count
        distance = speed * (max_time-count)
        if distance > target_distance:
            result = f"* {count} : {distance}  {speed}"
            ways = ways + 1
        else:
            result = f"  {count} : {distance}  {speed}"
        print(result)
    return ways


total_ways = []
for index,time in enumerate(times):
    total_ways.append( calcVariations(time,distances[index]) ) 
    print("-----------------------------")
print(total_ways)
result = np.prod(np.array(total_ways))
print(result)


