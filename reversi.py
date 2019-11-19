#
# Ryan Wood ()
# FIT1045 Algorithms and Programming in Python, S1-2019 Assignment 1

# Usage python reversi.py

# Number of rows & cols in the square
board_size = 8

# Array of rows / identifiers
pos = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Each Player's icons, 1st is Blank, 2nd is P1, 3rd is P2
chars = [" ", "X", "O"]


# Create a new board item
def new_board():
    # Blank array to contain all the coordinates
    board = []

    # loop through the range (Board size) and create a array for each row
    for i in range(board_size):
        # Add an array to the board for each col
        board.append([' '] * board_size)

    # Give the caller the board array
    return board


def set_stone_at_location(player, pos1, pos2):
    # Array  #pos1 #pos2        #player num
    mainBoard[pos1][pos2] = chars[player]
    return


# Check if move is valid (Add the rules here)
def invalid_move(player, pos1, pos2):
    # Local var for is the move is valid - To be updated
    invalid = 0

    # Check if Array of rows contains pos1
    if pos1 not in pos:
        # Mark the move as invalid
        invalid = 1

    # Check if pos2 exists on the board (Check number vs's board size)
    if pos2 > board_size:
        # Mark the move as invalid
        invalid = 1

    # Check that the position is not already claimed
    if mainBoard[pos.index(pos1)][pos2-1] != chars[0]:
        # Mark the move as invalid
        invalid = 1

    # Return the valid state
    return invalid


# Small function split a word at each char
def split(word):
    # Loop through word and create an array for each char
    return [char for char in word]


# Put the default stones into the board
def reset_board(board):

    # loop through all possible co-ordinates and set them to the blank char
    for x in range(board_size):
        for y in range(board_size):
            # Set the position to be a blank char
            board[x][y] = chars[0]

    # Default stones
    board[3][3] = chars[2]
    board[4][4] = chars[2]
    board[3][4] = chars[1]
    board[4][3] = chars[1]


def print_board(board):
    # Formatting of the box
    # Top of the game
    title = '    _______________________________ '

    # Splitter of each row
    header = '   |---|---|---|---|---|---|---|---|'

    # Bottom of the game
    footer = '   |___|___|___|___|___|___|___|___|'

    # Print top positions
    print('     a   b   c   d   e   f   g   h')

    # Value for the iterator
    i = 0

    # Print the top of the game
    print(title)

    # Loop through Y axis
    for y in range(board_size):
        # Add one to the iterator
        i += 1

        # Check if this is the first iteration
        if i > 1:
            print(header)

        # Print the left side counter
        print(' %s ' % i, end='')

        # Loop through X axis
        for x in range(board_size):
            # Print the box with the stone inside (Convert array into interface)
            print('| %s ' % (board[x][y]), end='')

        # Right hand side closing line
        print('|', end='')

        # Create new line
        print("")

    # Print the bottom of the game
    print(footer)


# Greeting to the game
print('Welcome to Reversi!')
print('By Ryan Wood')


# Create mainBoard
mainBoard = new_board()

# Reset the board
reset_board(mainBoard)

# Determine starting player
turn = "player1"

# Inform user who the starting player will be
print('Player 1 will go first\r\n\r\n')

# Begin the game loop
while True:

    # Check whos turn it is to play.
    if turn == 'player1':

        # Display the board to the user
        print_board(mainBoard)

        # Prompt the user for their next position
        nextPos = input("\r\nPlayer 1: ")

        # Convert user input into an array.
        nextPos = split(nextPos)

        # Check that move is valid (Call function to check)
        if invalid_move(turn, nextPos[0], int(nextPos[1])) == 1:

            # Inform the user the move is invalid.
            print("Invalid Move.")

        else:
            # Change the stone at desired co-ordinates
            set_stone_at_location(1, (pos.index(nextPos[0])), int(nextPos[1]) - 1)

            # If move is valid. Continue
            turn = 'player2'

    elif turn == 'player2':

        # Display the board to the user
        print_board(mainBoard)

        # Prompt the user for their next position
        nextPos = input("\r\nPlayer 2: ")

        # Convert user input into an array.
        nextPos = split(nextPos)

        # Check that move is valid (Call function to check)
        if invalid_move(turn, nextPos[0], int(nextPos[1])) == 1:

            # Inform the user the move is invalid.
            print("Invalid Move.")

        else:
            # Change the stone at desired co-ordinates
            set_stone_at_location(2, (pos.index(nextPos[0])), int(nextPos[1]) - 1)

            # If move is valid. Continue
            turn = 'player1'

