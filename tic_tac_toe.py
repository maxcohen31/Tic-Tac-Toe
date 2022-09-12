# Tic Tac Toe using numpy
# Even though the game is working fine, the code can be quite improved. By now is more compless than it could be
# Any further improvement is well accepted
# Author: Emanuele

import numpy as np
import random


# Setting up the board
grid = np.array([[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])


# Making the turn variable
turn = 0

# Number of moves allowed
max_moves = 9

# This function will randomly choice a player to start the game with
def toss_the_coin():
    global turn
    coin = random.randint(0, 2)

    if coin == 1:
        print('Player1 starts!')
        turn = 1
    elif coin == 2:
        print('Player2 starts!')
        turn = 2

# The flip_player function switches the players
def flip_player():
    global turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1

# Check for winner
def winner():
    for x in range(3):
        if grid[x][0] == 1 and grid[x][1] == 1 and grid[x][2] == 1: # Loop through the rows and report if the player1 have won
            print('Player1 won!')
            return True
    for x in range(3):
        if grid[x][0] == 2 and grid[x][1] == 2 and grid[x][2] == 2: # Loop through the rows and report if the player2 have won
            print('Player2 won!')
            return True
    for x in range(3):
        if grid[0][x] == 1 and grid[1][x] == 1 and grid[2][x] == 1: # Loop through the columns and report if the player1 have won
            print('Player1 won!')
            return True       
    for x in range(3):
        if grid[0][x] == 2 and grid[1][x] == 2 and grid[2][x] == 2: # Loop through the columns and report if the player2 have won
            print('Player2 won!')
            return True             
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1: # Loop through the diagonals and report if the player1 have won
        print('Player1 won!')
        return True
    if grid[0][0] == 2 and grid[1][1] == 2 and grid[2][2] == 2: # Loop through the diagonals and report if the player2 have won
        print('Player2 won!')
        return True
    return False
        
# Function to update the grid
def grid_add(row, col, n):
    grid[row][col] = n
    print(grid)
        
# Main logic
def game():
    toss_the_coin() # Calling the toss_the_coin function to select wich player will start to play
    global grid, max_moves, turn
    while max_moves > 0: # moves allowed before the game goes to an end
        if turn == 1: # Player1 turn
            try:
                player1_row = int(input('Player1 pick up a row from 1-3: ')) - 1 # Selecting the row
                player1_col = int(input('Player1 select a column from 1-3: ')) - 1 # Selecting the column
                if grid[player1_row][player1_col] == 1 or grid[player1_row][player1_col] == 2: # Check if is a valid move. If not, play again
                    turn = 1
                    print(' Move not allowed. Pick up another slot')
                else:
                    grid_add(player1_row, player1_col, 1) # if the move is valid flip_player function has called
                    flip_player()
                    max_moves -= 1  
            except IndexError: # If the player select a wrong row or column, player1 is prompted to play again
                print('Player1 select a correct row and column') 
                player1_row = int(input('Player1 pick up a row from 1-3: ')) - 1
                player1_col = int(input('Player1 select a column from 1-3: ')) - 1
                grid_add(player1_row, player1_col, 1)   
                flip_player() 
            if winner():
                break
        if turn == 2: # Player2 turn
            try:
                player2_row = int(input('Player2 pick up a row from 1-3: ')) - 1
                player2_col = int(input('Player2 select a column from 1-3: ')) - 1
                if grid[player2_row][player2_col] == 1 or grid[player1_row][player1_col] == 2:
                    turn = 2
                    print('Move not allowed. Pick another slot')
                else:
                    grid_add(player2_row, player2_col, 2)  
                    flip_player()
                    max_moves -= 1
            except IndexError:
                print('Player2 select a correct row and column')
                player2_row = int(input('Player2 pick up a row from 1-3: ')) - 1
                player2_col = int(input('Player2 select a column from 1-3: ')) - 1
                grid_add(player2_row, player2_col, 2)   
                flip_player()
            if winner():
                break
            not winner() and max_moves == 0: # If a winner has not yet found then there is tie
            print('Tie!')       

# Main driver
if __name__ == '__main__':               
    game()

