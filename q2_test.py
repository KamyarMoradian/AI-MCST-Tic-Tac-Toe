from q2 import find_best_move


def test1():
    board = [
        ['X', 'X', '_'],
        ['_', 'O', '_'],
        ['_', '_', '_']
    ]
    best_move = find_best_move(board)
    assert best_move == [0, 2]


def test2():
    board = [
        ['X', 'X', 'O'],
        ['_', 'O', '_'],
        ['X', '_', '_']
    ]
    best_move = find_best_move(board)
    assert best_move == [1, 0]


def test3():
    board = [
        ['X', 'X', 'O'],
        ['O', 'O', '_'],
        ['X', 'X', '_']
    ]
    best_move = find_best_move(board)
    assert best_move == [1, 2]


def test4():
    board = [
        ['X', '_', 'O'],
        ['_', '_', '_'],
        ['_', '_', 'X']
    ]
    best_move = find_best_move(board)
    assert best_move == [1, 1]


def test5():
    board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'X'],
        ['O', '_', '_']
    ]
    best_move = find_best_move(board)
    assert best_move == [2, 1]
