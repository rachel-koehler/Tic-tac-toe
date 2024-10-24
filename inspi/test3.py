def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")

# Test the print_board function:
# print_board([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])

def player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move as 'row,col': ")
            row, col = map(int, move.split(","))
            if (
                row >= 1
                and row <= 3
                and col >= 1
                and col <= 3
                and board[row - 1][col - 1] == " "
            ):
                board[row - 1][col - 1] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print(
                "Invalid input. Please enter row and column as 'row,col' (e.g., 2,3)."
            )
        except IndexError:
            print("Invalid input. Row and column must be between 1 and 3.")

def check_win(board):
    # Check horizontal, vertical, and diagonal lines for a win
    lines = []
    lines.extend(board)  # horizontal lines
    lines.extend(zip(*board))  # vertical lines
    lines.append([board[i][i] for i in range(3)])  # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # secondary diagonal

    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return True
    return False

def check_win(board):
    # Check horizontal, vertical, and diagonal lines for a win
    lines = []
    lines.extend(board)  # horizontal lines
    lines.extend(zip(*board))  # vertical lines
    lines.append([board[i][i] for i in range(3)])  # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # secondary diagonal

    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    print("Game over!")

# Start the game
play_game()