import numpy as np


def evaluate_1(matrix):
    board = np.flip(np.fliplr(matrix))
    score = 12
    for i, row in enumerate(board):
        ai_pieces = [j for j, p in enumerate(row) if p == 'C']
        player_pieces = [j for j, p in enumerate(row) if p == 'O']
        score -= len(ai_pieces) * i + len(player_pieces) * i
    return score
