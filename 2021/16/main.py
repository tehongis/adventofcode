import binascii

f = open('input.txt')
signal = f.readlines()
f.close()

hexdict={
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
        }


bitstream = ''

for number in signal[0].strip():
    bits = hexdict[number]
    bitstream=bitstream+bits

def read3bits(stream,index):
    valuestr = stream[index]+stream[index+1]+stream[index+2]
    value = int(valuestr,2)
    return (index,value)    

index = 0
index, value = read3bits(bitstream,index)
index, value2 = read3bits(bitstream,index)
print(value,value2)

