#Tic Tac Toe
#By Aaron Sears

from __future__ import print_function
import random
from classes import user
from classes import gameboard


def drawBoard(board):
    print(board.getSpace(1) + ' | ' + board.getSpace(2) + ' | ' + board.getSpace(3))
    print('---------')
    print(board.getSpace(4) + ' | ' + board.getSpace(5) + ' | ' + board.getSpace(6))
    print('---------')
    print(board.getSpace(7) + ' | ' + board.getSpace(8) + ' | ' + board.getSpace(9))

def inputNamePlayer1():
    name = raw_input('Player 1: Please enter your name: ')
    return name

def inputNamePlayer2():
    Name = raw_input('Player 2: Please enter your name: ')
    return Name

def inputSymbol():
    correctinput = True
    while correctinput:
        symbol = raw_input('Please choose a letter (X or O): ').upper()
        if symbol != 'X' and symbol != 'O':
            print('Invalid Letter')
        else:
            correctinput = False
    return symbol

def randomizeFirstPlayer():
    if random.randint(0,1) == 0:
        print(player1.username + ' goes first!')
        return player1.getSymbol()
    else:
        print(player2.username + ' goes first!')
        return player2.getSymbol()

def makeMove(symbol):
    selection = input('Please select a square to make your move (1-9): ')
    if checkLocation(selection):
        gameBoard.changeboard(selection, symbol)
        drawBoard(gameBoard)
        return symbol
    else:
        makeMove(symbol)

def checkLocation(square):
    if gameBoard.getSpace(square) == (' '):
        return True
    else:
        print('Space is already taken')
        return False

def winner(board):
    if board.getSpace(1) == board.getSpace(2) and board.getSpace(2) == board.getSpace(3) and board.getSpace(1) != ' ':
        return True
    elif board.getSpace(4) == board.getSpace(5) and board.getSpace(5) == board.getSpace(6) and board.getSpace(4) != ' ':
        return True
    elif board.getSpace(7) == board.getSpace(8) and board.getSpace(8) == board.getSpace(9) and board.getSpace(7) != ' ':
        return True
    elif board.getSpace(1) == board.getSpace(4) and board.getSpace(4) == board.getSpace(7) and board.getSpace(1) != ' ':
        return True
    elif board.getSpace(2) == board.getSpace(5) and board.getSpace(5) == board.getSpace(8) and board.getSpace(2) != ' ':
        return True
    elif board.getSpace(3) == board.getSpace(6) and board.getSpace(6) == board.getSpace(9) and board.getSpace(3) != ' ':
        return True
    elif board.getSpace(1) == board.getSpace(5) and board.getSpace(5) == board.getSpace(9) and board.getSpace(1) != ' ':
        return True
    elif board.getSpace(3) == board.getSpace(5) and board.getSpace(5) == board.getSpace(7) and board.getSpace(3) != ' ':
        return True
    else:
        return False

def playagain():
    correctinput = True
    while correctinput:
        replay = raw_input('Would you like to play again? (Y or N): ').upper()
        if replay != 'Y' and replay != 'N':
            print('Invalid input')
        else:
            correctinput = False
    return replay
    

#Main Function
player1 = user(inputNamePlayer1())
player1.setSymbol(inputSymbol())
player2 = user(inputNamePlayer2())
if player1.getSymbol() == 'X':
    player2.setSymbol('O')
else:
    player2.setSymbol('X')

gameBoard = gameboard()
count = 0
state = 1
while state:
    if count == 0:
        gameBoard.reset()
        drawBoard(gameBoard)
        lastMove = makeMove(randomizeFirstPlayer())
    elif lastMove == player1.getSymbol():
        print(player2.username + ':')
        lastMove = makeMove(player2.getSymbol())
    else:
        print(player1.username + ':')
        lastMove = makeMove(player1.getSymbol())
    count += 1

    if count > 4 and winner(gameBoard):
        if lastMove == player1.getSymbol():
            print(player1.username + ' Wins!')
            replay = playagain()
            if replay == 'Y':
                count = 0
            else:
                state = 0
        else:
            print(player2.username + ' Wins!')
            replay = playagain()
            if replay == 'Y':
                count = 0
            else:
                state = 0
    elif count >= 9:
        replay = playagain()
        if replay == 'Y':
            count = 0
        else:
            state = 0

print('Game Over!')

