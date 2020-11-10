import numpy as np
from board import get_all_moves_from, apply_change
from evaluate import evaluate_1


class DefaultStrategy:
    def __init__(self):
        pass

    def __call__(self, matrix, ai_player):
        lst = get_all_moves_from(matrix, ai_player)
        values = [evaluate_1(apply_change(matrix, ai_player, mv)) for mv in lst]
        return lst[values.index(max(values))]
