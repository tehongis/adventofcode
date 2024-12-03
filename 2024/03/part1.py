
from pprint import pprint
import re 

"""
However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

"do()"
"don't()"

"""

pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
nrpattern = r'\d+'

result = 0
enabled=True
with open("input.txt", "r") as infile:
    data=infile.read()

    matches = re.findall(pattern, data)
    for match in matches:
        pprint(match)
        if "do()" in match:
            enabled=True
        elif "don't()" in match:
            enabled=False
        elif "mul" in match:
            numbers = re.findall(nrpattern, match)[:2]
            numbers = list(map(int, numbers))
            #pprint(numbers)
            value = numbers[0]*numbers[1]
            if enabled:
                result = result + value
pprint(result)
