# TIC-TAC-TOE
# This is a 2-player game.

import os
import random

# Clears output screen
def clear():
    os.system('cls')

# Displaying Game Board
# Size of board should be 10 (not 9).
# Bcoz we are using index from 1-9.
def display_board(board):

    clear()
    print('\n %s | %s | %s ' %(board[7],board[8],board[9]))
    print('-----------')
    print(' %s | %s | %s ' %(board[4],board[5],board[6]))
    print('-----------')
    print(' %s | %s | %s \n' %(board[1],board[2],board[3]))


def player_input():
    marker = ''   #empty string

# Loops runs until input is either X or O.
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: X or O? ').upper()

# Returning marker choices as Tuple
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Prints player's move on the board
def place_marker(board, marker, position):
    board[position] = marker

# Function to check completion of game.
def check_winner(board, mark):
# Various cases to win a game.
    if (board[1]==mark and board[2]==mark and board[3]==mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark):
        return True

# Randomly choosing which player starts the play.
def first_player():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Checks occupancy of current position.
def check_space(board, position):
    if board[position] == ' ':
        return True

# Checks board for DRAW.
def board_check(board):

    for i in range(1,10):
        if check_space(board,i):
            return False

    return True

# Making choice.
def move_choice(board,player):
    position = ' '

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(board, int(position)):
        position = input('%s, Choose your next move (1-9): ' %player)

    return int(position)

def play_again():
    choice = input('Do you want to play again? (Yes/No) ').upper()
    if choice == 'YES':
        return True
    else:
        return False

# Game Driver Code:
print('TIC-TAC-TOE')
print('How to play?\nEnter the position number to make your move.')
print('\n 7 | 8 | 9 ')
print('-----------')
print(' 4 | 5 | 6 ')
print('-----------')
print(' 1 | 2 | 3 \n')

while True:
    the_board = [' ']*10
# player_input() returns a Tuple.
    player1_marker, player2_marker = player_input()

    turn = first_player()
    print('%s will the game.' %turn)

    game_on = True

    while game_on:
        if turn == "Player 1":
            # Player 1 Turn
            display_board(the_board)
            position = move_choice(the_board, 'Player 1')
            place_marker(the_board,player1_marker,position)

            if check_winner(the_board,player1_marker):
                display_board(the_board)
                print('Congrats! Player 1 Won')
                game_on = False

            else:
                if board_check(the_board):
                    display_board(the_board)
                    print('DRAW!')
                    game_on = False

                else:
                    turn = "Player 2"

        else:
            # Player 2 Turn
            display_board(the_board)
            position = move_choice(the_board, 'Player 2')
            place_marker(the_board, player2_marker, position)

            if check_winner(the_board,player2_marker):
                display_board(the_board)
                print('Congrats! Player 2 Won')
                game_on = False

            else:
                if board_check(the_board):
                    display_board(the_board)
                    print('DRAW!')
                    game_on = False

                else:
                    turn = "Player 1"

    if not play_again():
        break








