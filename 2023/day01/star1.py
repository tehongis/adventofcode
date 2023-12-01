from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

total = 0
for line in inputdata:
    line=line.strip()
    all_numbers = re.findall(r'\d', line)

    first_number = all_numbers[0]
    last_number =  all_numbers[-1]

    two_digits = first_number+last_number
    total = total + int(two_digits)

print(total)

