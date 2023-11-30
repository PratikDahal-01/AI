import random

board = [' ' for _ in range(9)]
HUMAN = 'X'
COMPUTER = 'O'
WINNING_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

def print_board(board):
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print(' | '.join(row))
        print('---------')

def check_win(board, player):
    for combo in WINNING_COMBINATIONS:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_empty_squares(board):
    return [i for i, val in enumerate(board) if val == ' ']

def minimax(board, depth, maximizing):
    if check_win(board, COMPUTER):
        return 1
    elif check_win(board, HUMAN):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing:
        best_score = -float('inf')
        for move in get_empty_squares(board):
            board[move] = COMPUTER
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_empty_squares(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def make_computer_move(board):
    best_score = -float('inf')
    best_move = None
    for move in get_empty_squares(board):
        board[move] = COMPUTER
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = COMPUTER

def main():
    print_board(board)
    while True:
        if not is_board_full(board):
            try:
                human_move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= human_move < 9 and board[human_move] == ' ':
                    board[human_move] = HUMAN
                else:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9")
                continue
        else:
            print("It's a draw!")
            break

        if check_win(board, HUMAN):
            print_board(board)
            print("You win!")
            break

        if not is_board_full(board):
            make_computer_move(board)
            print_board(board)
        else:
            print("It's a draw!")
            break

        if check_win(board, COMPUTER):
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()
