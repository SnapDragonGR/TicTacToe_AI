# Initial skeleton of the game


def board_gen():
    return [[0 for i in range(3)] for j in range(3)]


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))


def assign_player():
    choice = input("Do you want to be X or O? ").lower().strip()
    if choice == 'x':
        player1 = 'X'
        player2 = 'O'
        print("Player 1 (X) goes first!")
    elif choice == 'o':
        player1 = 'O'
        player2 = 'X'
        print("Player 2 (O) goes first!")
    else:
        print("Invalid input. Please try again.")
        return assign_player()

    return player1, player2


def get_move():
    move = input("Choose where to make your move (Row Column): ").strip()

    if move not in ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']:
        print("Invalid range. Please try again.")
        return get_move()

    return move


def make_move(board, coordinates, player1, player2):
    coordinates = coordinates.split()
    row = coordinates[0]
    column = coordinates[1]
    board[int(row) - 1][int(column) - 1] = player1 if player1 else player2


def get_winner(board):
    pass


def is_board_full(board):
    pass


board = board_gen()
score = []

# Game loop until the game_over function returns True
winner = False
while not winner:
    player1 = False
    player2 = False
    # Player assignment
    if not (player1 and player2):
        player1, player2 = assign_player()

    # Print the board
    print_board(board)

    # Get the coords of the move first
    coordinates = get_move()

    # Transfer the coords to the board
    make_move(board, coordinates, player1, player2)

    # This func breaks the loop + determines the winner
    winner = get_winner(board)

    # Breaks the loop if it's a draw
    if is_board_full(board):
        print("It's a draw!")
        winner = True
