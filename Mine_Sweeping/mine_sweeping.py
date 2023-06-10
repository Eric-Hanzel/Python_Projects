import random

"""Converts the input string to a list (coordinates)"""


def enter_to_move(enter):
    move = []
    for i in enter:
        move.append(i)
    move[0] = ord(move[0]) - 65
    move[1] = int(move[1])
    return move


"""Generate mine location"""


def generate_mine(d):
    total_mines = [10, 40, 99]
    mine_positions = []
    i = 0
    while i != total_mines[d - 1]:
        a = random.randint(0, (d * 8) - 1)
        b = random.randint(0, (d * 8) - 1)
        position = [a, b]
        if position not in mine_positions:
            mine_positions.append(position)
            i = i + 1
    return mine_positions


"""Detect several mines around"""


def check_around(move, mine_positions):
    check_position = [[1, 0], [1, 1], [0, 1], [-1, -1], [-1, 0], [0, -1], [-1, 1], [1, -1]]
    mine_total = 0
    i = 0
    while i != 8:
        if coordinate_addition(move, check_position[i]) in mine_positions:
            mine_total = mine_total + 1
            i = i + 1
        else:
            i = i + 1
    return mine_total


"""Sum of coordinates"""


def coordinate_addition(l1, l2):
    l3 = [0, 0]
    l3[0] = l1[0] + l2[0]
    l3[1] = l1[1] + l2[1]
    return l3


"""Change the number displayed on the board"""


def change_mine_board(symbol, move, tm):
    m1 = move[0]
    m2 = move[1]
    symbol[m1][m2] = str(tm) # Show the total number of mines surrounding
    return symbol


"""Print the number of statistics on the chessboard.
About mines, flags and no visible squares."""


def print_statistics(symbol, d):
    total_mines = [10, 40, 99]
    i = 0
    total_flags = 0 # Total number of flags
    total_novisible = 0 # Total number of no visible squares
    while i != d * 8:
        j = 0
        while j != d * 8:
            if symbol[i][j] == "F":
                total_flags = total_flags + 1 # Count the total number of flags
            elif symbol[i][j] == " ":
                total_novisible = total_novisible + 1
            j = j + 1
        i = i + 1
    total_novisible = total_novisible + total_flags # Count the total number of no visible squares
    mines = total_mines[d - 1] - total_flags # Total number of mines
    print("Mines: " + str(mines), end="     ")
    print("Flags: " + str(total_flags), end="     ")
    print("No visible squares: " + str(total_novisible))
    return total_novisible # Returns the total number of unknown squares


"""Print checkerboard to screen"""


def print_mine_board(d, symbol):
    total_mines = [10, 40, 99]
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X"]
    if print_statistics(symbol, d) == total_mines[d - 1]: # Print the status bar and check if the game is won
        return False
    print("   ", end="")
    for i in range(0, d * 8):
        if i < 10:
            print("  " + str(i) + " ", end="")
        else:
            print(" " + str(i) + " ", end="")
    print()
    print("   ", end="")
    print("+---" * d * 8 + "+")
    # Above is the printed dividing line
    i = 0
    while i != d * 8:
        print(str(column[i]) + "  ", end="")
        j = 0
        while j != d * 8:
            print("| " + str(symbol[i][j]) + " ", end="")
            j = j + 1
        print("|")
        print("   ", end="")
        print("+---" * d * 8 + "+")
        i = i + 1
    # The above is to print a list of checkerboards

"""Dig blocks and display the results in three categories.
First, dig straight to the thunder and the game is over;
Second, this square has no mines and shows several mines around it;
Third, if the block has not been mined, and there are no mines in the surrounding eight blocks, 
repeat the mining operation to the surrounding blocks."""


def dig_mine(move, mine_positions, symbol):
    if move in mine_positions: # First kind
        return False
    else:
        if check_around(move, mine_positions) > 0: # Second kind
            total_mines = check_around(move, mine_positions) # total mines
            return change_mine_board(symbol, move, total_mines)
        elif check_around(move, mine_positions) == 0: # Third kind
            total_mines = 0
            symbol = change_mine_board(symbol, move, total_mines)
            check_position = [[1, 0], [1, 1], [0, 1], [-1, -1], [-1, 0], [0, -1], [-1, 1], [1, -1]]
            i = 0
            while i != 8: # repeat the mining operation to the surrounding blocks.
                Next_position = coordinate_addition(move, check_position[i])
                if 0 <= Next_position[0] < d * 8 and 0 <= Next_position[1] < d * 8 and symbol[Next_position[0]][Next_position[1]] == " ":
                    # Check whether the operating point is within range and not already operated
                    symbol = dig_mine(Next_position, mine_positions, symbol)
                i = i + 1
            return symbol


print("Welcome to Minesweeper.")
print("Please choose your difficulty: ")
print("  1:Beginner 8 x 8 grid with 10 mines.")
print("  2:Intermediate 16 x 16 grid with 40 mines.")
print("  3:Expert 24 x 24 grid with 99 mines.")
d = int(input())  # Game Difficulty Selection
mine_positions = generate_mine(d)  # Generate mines
symbol = [[" "] * d * 8 for i in
          range(d * 8)]  # Generates a two-dimensional array to represent the state of each square
game = True
print_mine_board(d, symbol)  # Print the initial chessboard
while game:
    tempt = input("Please choose move, label or delete label: ")
    if tempt == "move":  # Select the mine-digging step
        enter = input("Please enter your move: ")
        move = enter_to_move(enter) # Converts the input string to a list (coordinates)
        symbol = dig_mine(move, mine_positions, symbol) # Change the two-dimensional array.
        if symbol == False: # Dig the mines
            print("Game over.")
            break
        if print_mine_board(d, symbol) == False: # Winning the game
            print("You win!!!")
            break
    elif tempt == "label": # Select flag
        enter = input("Please enter the position of your label: ")
        position = enter_to_move(enter)
        if symbol[position[0]][position[1]] == " ":
            symbol = change_mine_board(symbol, position, "F")
        print_mine_board(d, symbol)
    elif tempt == "delete label": # Select Delete Flag
        enter = input("Please enter the position of the label that you want to delete: ")
        position = enter_to_move(enter)
        if symbol[position[0]][position[1]] == "F":
            symbol = change_mine_board(symbol, position, " ")
        print_mine_board(d, symbol)
    else: # input error
        print("Please enter move, label or delete label.")
