# Initial skeleton of the game

def board_gen():
    return [[0 for i in range(3)] for j in range(3)]


def print_board(board):
    for row in board:
        print(row)


def assign_player():
    choice = input("Do you want to be X or O? ").lower()
    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'


def display_players():
    pass

board = board_gen()
score = []

# Game loop until the game_over function returns True
while not winner:
    # Player assignment
    if not players:
        assign_player()
        display_players()

    # Print the board
    print_board(board)

    # Get the coords of the move first
    coordinates = get_move()

    # Transfer the coords to the board
    make_move(board, coordinates, player)

    # This func breaks the loop + determines the winner
    winner = get_winner(board)

    # Breaks the loop if it's a draw
    if is_board_full(board):
        print("It's a draw!")
        winner = True