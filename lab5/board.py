import json
from itertools import permutations

import numpy as np

EMP = ' '


def get_default_board():
    return [
        ['C', 'C', 'C', 'C'],
        [EMP, EMP, EMP, EMP],
        [EMP, EMP, EMP, EMP],
        ['O', 'O', 'O', 'O'],
    ]


def is_final_state(matrix):
    return matrix[0] == ['O', 'O', 'O', 'O'] or matrix[3] == ['C', 'C', 'C', 'C']


class InvalidMove(Exception):
    pass


def is_valid_move(board, player, move, throw=True):
    try:
        if not (0 <= move[0][0] <= 3 and 0 <= move[0][1] <= 3 and 0 <= move[1][0] <= 3 and 0 <= move[1][1] <= 3):
            raise InvalidMove("Move is outside range")
        if board[move[0][0]][move[0][1]] != player:
            raise InvalidMove("The chose piece is not the current player's")
        if board[move[1][0]][move[1][1]] != EMP:
            raise InvalidMove("That space is not empty")
        if abs(move[0][0] - move[1][0]) not in [0, 1] or \
                abs(move[0][1] - move[1][1]) not in [0, 1]:
            raise InvalidMove("Move is only allowed 1 space")
        if move[0][0] == move[1][0] and move[0][1] == move[1][1]:
            raise InvalidMove("Same move not allowed")
    except InvalidMove as e:
        if throw:
            raise e
        else:
            return False
    return True


def get_all_moves_from(matrix, player):
    all_moves = []
    dst = []
    for x in [0, 1, -1]:
        for j in [0, 1, -1]:
            dst.append([x, j])

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == player:
                all_moves += [[[i, j], [i + add[0], j + add[1]]] for add in dst
                              if is_valid_move(matrix, player, [[i, j], [i + add[0], j + add[1]]], False)]
    return all_moves


def apply_change(board, player, move):
    new_board = json.loads(json.dumps(board))
    is_valid_move(board, player, move)
    new_board[move[0][0]][move[0][1]] = EMP
    new_board[move[1][0]][move[1][1]] = player
    return new_board
