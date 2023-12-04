from pprint import pprint

import re

f = open('input.txt','r')
inputdata = f.readlines()
f.close()

def locate_symbols():
    symbols = []
    for row_number,line in enumerate(inputdata):
        line = line.strip()
        line_symbols = []
        for index,char in enumerate(line):
            if char == '.':
                continue
            if char.isnumeric():
                continue
            line_symbols.append(index)
        symbols.append( (row_number,line_symbols) )
#            out = f"{row_number}-{index}:{char}"
#            print(out)
    return symbols

def locate_numbers():
    numbers = []
    for row_number,line in enumerate(inputdata):
        line = line.strip()
        for number in re.finditer(r'\d+', line):
            print(number.span())
            numbers.append( (row_number,number.span(),int(number.group())) )
    return numbers


pprint( locate_numbers() )
pprint( locate_symbols() )
