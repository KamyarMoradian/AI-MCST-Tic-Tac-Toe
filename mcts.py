import math
import utills
from node import Node


class MCTS:
    def __init__(self, root, c_const=2.0, iterations=1000):
        self.root = root
        self.c_const = c_const
        self.iterations = iterations

    def ucb(self, node):
        return node.value / node.times_visited + self.c_const \
               * math.sqrt(math.log(node.parent.times_visited) / node.times_visited)

    def max_ucb_child(self, node):
        return max(node.children, key=lambda child_node: self.ucb(child_node))

    def select(self, node):
        while True:
            if node.times_visited == 0 or utills.is_terminal(node.state) or node.is_leaf():
                return node

            else:
                for child in node.children:
                    if child.times_visited == 0:
                        return child

            node = self.max_ucb_child(node)

    def simulate(self, node):
        current_board = utills.copy_board(node.state)
        turn = 1

        while True:
            # calculate the score if the game is over
            if utills.is_terminal(current_board):
                return utills.get_score(current_board, turn)

            # Choose a random move
            row, col = utills.find_random(current_board)

            # Make the move and switch turns
            if turn == 0:
                current_board[row][col] = 'X'
                turn = 1
            else:
                current_board[row][col] = 'O'
                turn = 0

    def playout(self):
        node = self.select(self.root)
        if not utills.is_terminal(node.state):
            node = node.expand()
        value = self.simulate(node)
        node.back_propagate(value)

    def get_best_move(self):
        for _ in range(self.iterations):
            self.playout()
        return self.root.max_child_score().action
