def drawBoard(spots):
    board = (f'|{spots[1]}|{spots[2]}|{spots[3]}|\n'
             f'|{spots[4]}|{spots[5]}|{spots[6]}|\n'
             f'|{spots[7]}|{spots[8]}|{spots[9]}|') 
    print(board)

def checkTurn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
    
def checkIfWin(spots):
    if (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
        return True
    elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False
    
#def main():
    #spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
    #drawBoard(spots)
    #checkTurn()
#main()