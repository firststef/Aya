import unittest
import numpy as np

from game import *


class TestLab5(unittest.TestCase):
    def test_evaulate_1(self):
        matrix = [
            ['O', 'O', 'O', 'O'],
            ['C', 'C', 'C', 'C'],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        matrix = np.flip(matrix)
        self.assertEqual(evaluate_1(matrix), -8)
        matrix = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['O', 'O', 'O', 'O'],
            ['C', 'C', 'C', 'C'],
        ]
        matrix = np.flip(matrix)
        self.assertEqual(evaluate_1(matrix), 8)


if __name__ == "__main__":
    unittest.main()