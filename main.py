def board_gen():
    # Generate a 3x3 board as a list of lists for easy access
    return [[' ' for i in range(3)] for j in range(3)]


def print_board(board):
    # Print column headers with dashes
    print("    " + "   ".join(str(i + 1) for i in range(len(board[0]))))  # Column numbers
    print("  " + "+---" * len(board[0]) + "+")  # Top border for columns

    for row_idx, row in enumerate(board):
        # Print row number with content
        print(f"{row_idx + 1} | " + " | ".join(map(str, row)) + " |")
        # Print separator line after each row
        print("  " + "+---" * 3 + "+")


def assign_player():
    choice = input("Do you want to be X or O? ").lower().strip()

    if choice == 'x':
        player1 = 'X'
        player2 = 'O'
        print("\nPlayer 1 (X) goes first!")
    elif choice == 'o':
        player1 = 'O'
        player2 = 'X'
        print("\nPlayer 2 (O) goes first!")
    else:
        # Error handling
        print("\nInvalid input. Please try again.")
        return assign_player()

    return player1, player2


def get_move(player):
    move = input(f"\n{player}, choose where to make your move (Row Column): ").strip()

    # Error handling
    if move not in ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']:
        print("\nInvalid range. Please try again.")
        return get_move(player)

    return move


def make_move(board, coordinates, player):
    # Split the input into two values for future board implementation
    coordinates = coordinates.split()
    row = int(coordinates[0])
    column = int(coordinates[1])

    # Check if the cell is empty
    if board[row - 1][column - 1] == ' ':
        board[int(row) - 1][int(column) - 1] = player
    else:
        print('\nThe cell is already occupied. Please try again.')
        new_coordinates = get_move(player)
        make_move(board, new_coordinates, player)


def get_winner(board):
    pass


def is_board_full(board):
    pass


board = board_gen()
score = []

# Game loop until the game_over function returns True
winner = False
player1 = False
player2 = False

while not winner:
    if not (player1 and player2):
        player1, player2 = assign_player()

    # Print the board
    print_board(board)

    # Get the coords of the move first
    player1_move = get_move(player1)

    # Transfer the coords to the board
    make_move(board, player1_move, player1)

    print_board(board)

    player2_move = get_move(player2)

    make_move(board, player2_move, player2)

    # This func breaks the loop + determines the winner
    winner = get_winner(board)

    # Breaks the loop if it's a draw
    if is_board_full(board):
        print("\nIt's a draw!")
        winner = True
