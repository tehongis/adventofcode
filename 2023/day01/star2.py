from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

#seven3lbcvjxqhhdpzkttqsixjzzjjbclfq1fiveeightwojx
['7', '3', '6', '1', '5', '2']

def name2number(rivi):
    rivi = rivi.replace('one','o1ne')
    rivi = rivi.replace('two','t2wo')
    rivi = rivi.replace('three','th3ree')
    rivi = rivi.replace('four','f4our')
    rivi = rivi.replace('five','f5ive')
    rivi = rivi.replace('six','s6ix')
    rivi = rivi.replace('seven','se7ven')
    rivi = rivi.replace('eight','eig8ht')
    rivi = rivi.replace('nine','ni9ne')
    return rivi
    

"""
valuedict = {
    
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        }
"""
total = 0
for line in inputdata:
    line=line.strip()
    print(line)

    line = name2number(line)
    
    all_numbers = re.findall(r'\d', line)

    first_number = all_numbers[0]
    last_number =  all_numbers[-1]

    two_digits = first_number+last_number

    print(all_numbers)

    total = total + int(two_digits)

print(total)

