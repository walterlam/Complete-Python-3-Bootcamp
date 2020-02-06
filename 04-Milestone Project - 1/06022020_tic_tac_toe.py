# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:30:05 2020

@author: walterlam
"""

'''
Python game: Tic-tac-toe
Background: 2 players take turns, insert a sign to board ('X' or 'O')
'''

# check whether the position is occupied
def check_blank(board,location):
    '''
    Return True if location is blank, False if occupied
    '''
    return board[location] == ' '

# used to display the board
def display_board(board):
    '''
    board display, given a list of all 
    '''
    print('         |         |         ')
    print('         |         |         ')
    print('    '+board[1]+'    |    '+board[2]+'    |    '+board[3]+'    ')
    print('         |         |         ')
    print('         |         |         ')
    print('---------+---------+---------')
    print('         |         |         ')
    print('         |         |         ')
    print('    '+board[4]+'    |    '+board[5]+'    |    '+board[6]+'    ')
    print('         |         |         ')
    print('         |         |         ')
    print('---------+---------+---------')
    print('         |         |         ')
    print('         |         |         ')
    print('    '+board[7]+'    |    '+board[8]+'    |    '+board[9]+'    ')
    print('         |         |         ')
    print('         |         |         ')

def check_board(board):
    '''
    return True if not all are occupied, False when all are occupied
    '''
    return (' ' in board)

def win_check(board, sign):
    '''
    check if that mark has won
    '''
    return (board[1] == sign and board[2] == sign and board[3] == sign) or\
    (board[4] == sign and board[5] == sign and board[6] == sign) or\
    (board[7] == sign and board[8] == sign and board[9] == sign) or\
    (board[1] == sign and board[4] == sign and board[7] == sign) or\
    (board[2] == sign and board[5] == sign and board[8] == sign) or\
    (board[3] == sign and board[6] == sign and board[9] == sign) or\
    (board[1] == sign and board[5] == sign and board[9] == sign) or\
    (board[3] == sign and board[5] == sign and board[7] == sign)

replay = True

while replay:
    # Welcome to the Tic-Tac-Toe game
    print('Welcome to the Tic-Tac-Toe game')
    board = ['#','1','2','3','4','5','6','7','8','9']
    display_board(board)
    
    # ask Player 1 to choose a sign ('X' or 'O')
    p1_sign = ' '
    p2_sign = ' '
    order = None
    while p1_sign not in ['X','O']:
        p1_sign = input('Player 1, choose your sign ("X" or "O"): ').upper()
    if p1_sign == 'X':
        p2_sign = 'O'
    else:
        p2_sign = 'X'
        
    # select who to start first by random
    import random
    if random.randint(0,1) == 0:
        print('Player 1 starts first')
        first = True
        order = [p1_sign,p2_sign,1]
    else:
        print('Player 2 starts first')
        first = False
        order = [p1_sign,p2_sign,2]
    
    # input
    
    # initialization
    playboard = [' ']*10
    playboard[0] = '#'
    
    # take in numeric value for next player
    newinput = 0
    
    if first:
        i = 0
    else:
        i = 1
        
    while check_board(playboard):
        while newinput not in range(1,10) or not check_blank(playboard,newinput):
            print("Player {}'s turn ({})".format(order[2],order[i]))
            newinput = int(input('Player, please pick one position: '))
            if newinput == 0:
                break
        # put in the location
        playboard[newinput] = order[i] # i can be 0 or 1
        display_board(playboard)
    
        if win_check(playboard,order[i]):
            print('Player {} wins'.format(order[2]))
            break

        # update i (to be 0 or 1)
        if i == 0:
            i += 1
            order[2] += 1
        else:
            i -= 1
            order[2] -= 1

    if not check_board(playboard):
        print('Draw! This is a tight game. Huh?')
    
    play_again = ' '
    while play_again not in ['T', 'F']:
        play_again = input('Wanna replay? (T/F)').upper()
    
    if play_again == 'T':
        continue
    else:
        break

        
    
    
    
    

