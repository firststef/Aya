import unittest

import numpy as np

from alphabetapruning_strategy import AlphaBetaPruningStrategy
from board import EMP
from game import Game
from minimax_strategy import *


class TestLab5(unittest.TestCase):
    def test_evaulate_1(self):
        matrix = [
            ['O', 'O', 'O', 'O'],
            ['C', 'C', 'C', 'C'],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        self.assertEqual(evaluate_1(matrix), -8)
        matrix = [
            ['O', 'O', 'O', 'O'],
            ['', 'C', 'C', 'C'],
            ['C', '', '', ''],
            ['', '', '', '']
        ]
        self.assertEqual(evaluate_1(matrix), -7)
        matrix = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['O', 'O', 'O', 'O'],
            ['C', 'C', 'C', 'C'],
        ]
        self.assertEqual(evaluate_1(matrix), 8)
        matrix = [
            ['', '', '', ''],
            ['', '', '', 'O'],
            ['O', 'O', 'O', ''],
            ['C', 'C', 'C', 'C'],
        ]
        self.assertEqual(evaluate_1(matrix), 7)
        matrix = [
            ['', '', '', ''],
            ['O', '', '', ''],
            ['', 'O', 'O', 'O'],
            ['C', 'C', 'C', 'C'],
        ]
        self.assertEqual(evaluate_1(matrix), 7)

    def test_minimax_simple_case(self):
        def evaluate_node(node, *args, **kwargs):
            if node == 'E':
                return 9
            if node == 'F':
                return -6
            if node == 'G':
                return 0
            if node == 'H':
                return -2
            if node == 'I':
                return -4
            if node == 'J':
                return -3

        def get_all_moves(node, *args, **kwargs):
            if node == 'A':
                return ['B', 'C', 'D']
            elif node == 'B':
                return ['E', 'F']
            elif node == 'C':
                return ['G', 'H']
            elif node == 'D':
                return ['I', 'J']
            else:
                return []

        def apply_move(state, turn, mv):
            return mv

        m = MiniMaxStrategy(2, evaluate_node, get_all_moves, apply_move)
        self.assertEqual(m('A', 'C'), 'C')

    def test_alphabeta_pruning_simple(self):
        def evaluate_node(node, *args, **kwargs):
            if node == 'D':
                return 3
            if node == 'E':
                return 5
            if node == 'F':
                return -5
            if node == 'G':
                raise Exception
            raise Exception

        def get_all_moves(node, *args, **kwargs):
            if node == 'B':
                return ['D', 'E']
            elif node == 'I':
                return ['K', 'L']
            elif node == 'F':
                return ['I', 'J']
            elif node == 'G':
                return ['M', 'N']
            elif node == 'C':
                return ['F', 'G', 'H']
            elif node == 'A':
                return ['B', 'B']
            else:
                return []

        def apply_move(state, turn, mv):
            return mv

        m = AlphaBetaPruningStrategy(2, evaluate_node, get_all_moves, apply_move)
        self.assertEqual(m('A', 'C'), 'B')

    def test_alphabeta_pruning_bigger(self):
        def evaluate_node(node, *args, **kwargs):
            if node == 'D':
                return 3
            if node == 'E':
                return 5
            if node == 'K':
                return 0
            if node == 'L':
                return 7
            if node == 'J':
                return 2
            if node == 'M':
                return 7
            if node == 'N':
                return 8
            if node == 'H':
                return 4
            raise Exception

        def get_all_moves(node, *args, **kwargs):
            if node == 'B':
                return ['D', 'E']
            elif node == 'I':
                return ['K', 'L']
            elif node == 'F':
                return ['I', 'J']
            elif node == 'G':
                return ['M', 'N']
            elif node == 'C':
                return ['F', 'G', 'H']
            elif node == 'A':
                return ['B', 'C']
            else:
                return []

        def apply_move(state, turn, mv):
            return mv

        m = AlphaBetaPruningStrategy(4, evaluate_node, get_all_moves, apply_move)
        self.assertEqual(m('A', 'C'), 'B')

    def test_ai(self):
        # g = Game("Computer", "Computer")
        # g.start()
        pass

    def test_allowed_move(self):
        self.maxDiff = 1000
        matrix = [
            [EMP, EMP, EMP, EMP],
            [EMP, EMP, EMP, EMP],
            [EMP, 'C', EMP, EMP],
            [EMP, EMP, EMP, EMP]
        ]
        matrix = np.flip(np.fliplr(matrix))
        a = get_all_moves_from(matrix, 'C')
        b = [
            [[1, 1], [1, 2]],
            [[1, 1], [1, 0]],
            [[1, 1], [0, 1]],
            [[1, 1], [2, 1]],
            [[1, 1], [0, 0]],
            [[1, 1], [2, 0]],
            [[1, 1], [2, 2]],
            [[1, 1], [0, 2]],
        ]
        self.assertCountEqual(a, b)


if __name__ == "__main__":
    unittest.main()