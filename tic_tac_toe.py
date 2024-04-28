EMPTY = '-'
X_PLAYER = 'X'
O_PLAYER = 'O'

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
=    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def game_over(board):
    return check_win(board, X_PLAYER) or check_win(board, O_PLAYER) or all(all(cell != EMPTY for cell in row) for row in board)

def evaluate(board):
    if check_win(board, X_PLAYER):
        return 1
    elif check_win(board, O_PLAYER):
        return -1
    else:
        return 0

# DFBB Algorithm with Alpha-Beta pruning
def dfbb(board, player, alpha, beta):
    if game_over(board):
        return evaluate(board)

    max_utility = float('-inf') if player == X_PLAYER else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = player
                utility = dfbb(board, X_PLAYER if player == O_PLAYER else O_PLAYER, alpha, beta)
                board[i][j] = EMPTY

                if player == X_PLAYER:
                    max_utility = max(max_utility, utility)
                    alpha = max(alpha, utility)
                else:
                    max_utility = min(max_utility, utility)
                    beta = min(beta, utility)

                if beta <= alpha:
                    break

    return max_utility

# Define function to find the best move using DFBB alpha-beta pruning
def find_best_move(board, player):
    best_move = None
    best_utility = float('-inf') if player == X_PLAYER else float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = player
                utility = dfbb(board, X_PLAYER if player == O_PLAYER else O_PLAYER, float('-inf'), float('inf'))
                board[i][j] = EMPTY

                if player == X_PLAYER and utility > best_utility:
                    best_move = (i, j)
                    best_utility = utility
                elif player == O_PLAYER and utility < best_utility:
                    best_move = (i, j)
                    best_utility = utility

    return best_move

# Define function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Define main function to play the game
def play_tic_tac_toe():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = X_PLAYER

    while not game_over(board):
        print_board(board)
        print(f"Player {current_player}'s turn.")

        if current_player == X_PLAYER:
            move = find_best_move(board, current_player)
            board[move[0]][move[1]] = X_PLAYER
        else:
            move = tuple(map(int, input("Enter row and column (0-2) separated by space: ").split()))
            board[move[0]][move[1]] = O_PLAYER

        current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER

    print_board(board)
    winner = evaluate(board)
    if winner == 1:
        print("Player X wins!")
    elif winner == -1:
        print("Player O wins!")
    else:
        print("It's a draw!")

# Start the game
play_tic_tac_toe()
