from utills import get_empty_spots, copy_board, check_win, is_moves_left
import random


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.value = 0
        self.times_visited = 0
        self.parent = parent
        self.children = []
        self.action = action

    def add_child(self, child):
        self.children.append(child)

    def update_value(self, value):
        self.value += value

    def update_times_visited(self):
        self.times_visited += 1

    def is_leaf(self):
        return len(self.children) == 0

    def expand(self):
        current_board = self.state
        empty_spots = get_empty_spots(current_board)
        for idx in empty_spots:
            row = int(idx/3)
            col = idx % 3
            new_board = copy_board(current_board)
            new_board[row][col] = 'X' if self.times_visited % 2 == 0 else 'O'
            new_node = Node(state=new_board, parent=self, action=[row, col])
            self.add_child(new_node)
        return random.choice(self.children)

    def back_propagate(self, value):
        self.update_value(value)
        self.update_times_visited()
        if self.parent is not None:
            self.parent.back_propagate(value)

    def max_child_score(self):
        return max(self.children, key=lambda child_node: child_node.value/child_node.times_visited)
