
import time

file = open('input.txt','r')
data = file.readlines()
file.close()

for index,item in enumerate(data):
    print(index,item.strip())
exit(0)

row_count = []

accumulator = 0
programcounter = 0

program_length = len(data)

running = True
while running:
    if programcounter not in row_count:
        row_count.append(programcounter)
    else:
        print("Final accumulator: ",accumulator)
        running = False
    line = data[programcounter].strip()
    command,parameter = line.split(' ')
    print(programcounter,accumulator,command,parameter)

    if command == 'acc':
        accumulator = accumulator + int(parameter)
        programcounter = programcounter + 1

    if command == 'nop':
        if programcounter+int(parameter) == program_length:
            print("This is the end!",programcounter,line)
            exit(0)
        programcounter = programcounter + 1

    if command == 'jmp':
        if programcounter + 1 == program_length:
            print("This is the end!",programcounter,line)
            exit(0)
        programcounter = programcounter + int(parameter)
    
    if programcounter >= program_length-1:
        print("Exit.")
        exit(0)

#    time.sleep(5)
