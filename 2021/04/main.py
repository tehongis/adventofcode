from pprint import pprint

def parsedata():
    f = open('input.txt','r')
    data = f.readlines()
    f.close()
    randoms = data[0].split(',')
    boards = []
    for row in zip(*[iter(data[1:])]*6):
        board = []
        board.append(row[1].strip().split())
        board.append(row[2].strip().split())
        board.append(row[3].strip().split())
        board.append(row[4].strip().split())
        board.append(row[5].strip().split())
        boards.append(board)
    return randoms,boards

def checklappu(lista,lappu):
    # vaaka
    for row in lappu:
        count = 0
        for number in row:
            if number in lista:
                count = count + 1
                if count == 5:
                    return True
    #pysty
    for columnnr in range(0,5):
        count = 0
        column = []
        column.append(lappu[0][columnnr])
        column.append(lappu[1][columnnr])
        column.append(lappu[2][columnnr])
        column.append(lappu[3][columnnr])
        column.append(lappu[4][columnnr])
        for number in column:
            if number in lista:
                count = count + 1
                if count == 5:
                    return True
    return False
            
def cleanlappu(lista,lappu):
    new_lappu = []
    for row in lappu:
        new_row=[]
        for number in row:
            if number in lista:
                new_row.append('*')
            else:
                new_row.append(number)
        new_lappu.append(new_row)
    return new_lappu

def calclappu(lappu):
    total = 0
    for row in lappu:
        for numbero in row:
            if numbero == '*':
                pass
            else:
                total = total + int(numbero)
    return total

randoms,boards = parsedata()

winnerboards=[]
lista = []
for numero in randoms:
    lista.append(numero)
    #print(f"Numero on: {numero}")
    for boardnr,board in enumerate(boards):
        if checklappu(lista,board):
            #pprint('BINGO!')                   
            tulos = cleanlappu(lista,board)
            #pprint(tulos)
            if boardnr not in winnerboards:
                winnerboards.append(boardnr)
                if len(winnerboards)==len(boards):
                    pprint(tulos)

                    numberoinen = calclappu(tulos)
                    print(numberoinen * int(numero) )   
    #print()
