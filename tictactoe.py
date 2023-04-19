#tiktactoe
import os
from helpertictactoe import drawBoard, checkTurn, checkIfWin
x = 'x'
o = 'o'
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
playing = True
win = False
turn = 0
previousTurn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    drawBoard(spots)

    if previousTurn == turn: #if invalid turn, lets player know
        print('Invalid spot selected, please pick another.')
    previousTurn = turn

    print('Player ' + str((turn % 2) + 1) + "'s turn: Pick your spot or press 'q' to quit!")
    choice = input() #input from player

    
    if choice == 'q':
        playing = False
    
    elif choice.isdigit(): #checks if number
        if int(choice) <= 9 and int(choice) >0: #checks if number is 1-9
            if not spots[int(choice)] in {'X', 'O'}: #checks if spot is taken
                turn += 1
                spots[int(choice)] = checkTurn(turn)

    if checkIfWin(spots): playing, win = False, True #check if win
    if turn > 8: playing = False #check if tie
os.system('cls' if os.name == 'nt' else 'clear')    
drawBoard(spots)
if  win:
    if checkTurn(turn) == 'X':
        print('Player 1 Wins!')
    else:
        print('Player 2 Wins!')
else:
    print('Tie Game. No Winner!')

print("Thanks for playing!")