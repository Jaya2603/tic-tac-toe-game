import random

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---------")
    print()

def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[idx] == player for idx in pattern) for pattern in win_patterns)

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(board, index, player):
    board[index] = player

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in get_available_moves(board):
                return move
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move(board):
    return random.choice(get_available_moves(board))

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'  # Player starts first

    while True:
        print_board(board)
        if current_player == 'X':
            move = player_move(board)
        else:
            move = computer_move(board)

        make_move(board, move, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif ' ' not in board:
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
