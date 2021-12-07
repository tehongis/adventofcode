file = open('day02.txt','r')
data = file.readlines()
file.close()

correct_count = 0

for line in data:
    line = line.rstrip()
    rule,password = line.split(':')
    password = password.strip(' ')
    numbers,letter = rule.split(' ')
    low,hi = numbers.split('-')
    low = int(low) - 1
    hi = int(hi) - 1
    print(rule,password,password[low],password[hi])
"""
    letter_count = password.count(letter)
    if low <= letter_count <= hi:
        print(rule,password)
        correct_count = correct_count + 1

print(correct_count)
"""
