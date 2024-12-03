from pprint import pprint

"""
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
"""

with open("input.txt", "r") as infile:
    data=infile.readlines()



def check_rising(values):
    for count in range(0,len(values)-1):
        a = values[count]
        b = values[count+1]
        if a == b:
            return False
        if a < b:
            return False
    return True

def check_lowering(values):
    for count in range(0,len(values)-1):
        a = values[count]
        b = values[count+1]
        if a == b:
            return False
        if a > b:
            return False
    return True

def check_diff(values):
    for count in range(0,len(values)-1):
        a = values[count]
        b = values[count+1]
        if a == b:
            return False
        if abs( a - b ) >3:
            return False
    return True


count = 0
for row in data:
    row = row.strip()
    values = [int(x) for x in row.split(' ')]
    pprint( values )
    if ( check_rising(values) or check_lowering(values) ) and check_diff(values):
        count = count + 1

print(count)
#    break