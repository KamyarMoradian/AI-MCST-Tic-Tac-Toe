from random import choice
from utills import find_random, is_moves_left, print_board, check_win
from mcts import MCTS
from node import Node

player, opponent = 'X', 'O'


def find_best_move(current_board):
    root = Node(state=current_board, parent=None, action=None)
    mcts_tree = MCTS(root=root, c_const=2, iterations=1000)
    best_move = mcts_tree.get_best_move()
    return best_move


if __name__ == "__main__":
    board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
    ]

    turn = 0

    while is_moves_left(board) and not check_win(board):
        if turn == 0:
            print_board(board)
            print(" Select Your Move :", end=" ")
            tmp = int(input())-1
            userMove = [int(tmp/3),  tmp % 3]
            while (userMove[0] < 0 or userMove[0] > 2) or (userMove[1] < 0 or userMove[1] > 2) \
                    or board[userMove[0]][userMove[1]] != "_":
                print('\n \x1b[0;33;91m' + ' Invalid move ' + '\x1b[0m \n')
                print("Select Your Move :", end=" ")
                tmp = int(input())-1
                userMove = [int(tmp/3),  tmp % 3]
            board[userMove[0]][userMove[1]] = player
            print("Player Move:")
            print_board(board)
            turn = 1
        else:
            bestMove = find_best_move(board)
            board[bestMove[0]][bestMove[1]] = opponent
            print("Agent Move:")
            print_board(board)
            turn = 0

    if check_win(board):
        if turn == 1:
            print('\n \x1b[6;30;42m' + ' Player Wins! ' + '\x1b[0m')

        else:
            print('\n \x1b[6;30;42m' + ' Agent Wins! ' + '\x1b[0m')
    else:
        print('\n \x1b[0;33;96m' + ' Draw! ' + '\x1b[0m')

    input('\n Press Enter to Exit... \n')
