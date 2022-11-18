from random import choice
import os


def check_win(current_board):
    for row in range(3):
        if current_board[row][0] == current_board[row][1] and current_board[row][1] == current_board[row][2]\
                and not current_board[row][0] == '_':
            return True
    for col in range(3):
        if current_board[0][col] == current_board[1][col] and current_board[1][col] == current_board[2][col]\
                and not current_board[0][col] == '_':
            return True

    if current_board[0][0] == current_board[1][1] and current_board[1][1] == current_board[2][2]\
            and not current_board[0][0] == '_':
        return True

    if current_board[0][2] == current_board[1][1] and current_board[1][1] == current_board[2][0]\
            and not current_board[0][2] == '_':
        return True

    return False


def is_moves_left(current_board):
    return '_' in current_board[0] or '_' in current_board[1] or '_' in current_board[2]


def is_terminal(state):
    return check_win(state) or not is_moves_left(state)


def get_score(current_state, turn):
    if check_win(current_state):
        if turn == 0:
            return -1
    return 1


def get_empty_spots(current_board):
    return [i * 3 + j for i in range(3) for j in range(3) if current_board[i][j] == "_"]


def find_random(current_board):
    empty_spots = get_empty_spots(current_board)
    idx = choice(empty_spots)
    return int(idx/3), idx % 3


def copy_board(current_board):
    return [current_board[i][:] for i in range(3)]


def print_board(current_board):
    os.system('cls||clear')
    print("\n Player : X , Agent: O \n")
    for i in range(3):
        print(" ", end=" ")
        for j in range(3):
            if current_board[i][j] == '_':
                print(f"[{i*3+j+1}]", end=" ")
            else:
                print(f" {current_board[i][j]} ", end=" ")
        print()
    print()
