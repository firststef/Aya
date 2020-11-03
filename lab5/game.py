# from abc import
import json
from typing import List
import numpy as np
import re

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


def is_valid_move(board, player, move, throw=True):
    try:
        if not (0 <= move[0][0] <= 3 and 0 <= move[0][1] <= 3 and 0 <= move[1][0] <= 3 and 0 <= move[1][1] <= 3):
            raise InvalidMove("Move is outside range")
        if board[move[0][0]][move[0][1]] != player:
            raise InvalidMove("The chose piece is not the current player's")
        if board[move[1][0]][move[1][1]] != EMP:
            raise InvalidMove("That space is not empty")
        if abs(move[0][0] - move[1][0]) not in [0, 1] or \
                abs(move[0][1] - move[1][1]) not in [0, 1] and \
                (abs(move[0][0] - move[1][0]) + abs(move[0][1] - move[1][1])) != 1:
            raise InvalidMove("Move is only allowed sideways")
    except InvalidMove as e:
        if throw:
            raise e
        else:
            return False
    return True


def get_all_moves_from(matrix, player):
    all_moves = []
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == player:
                all_moves += [[[i, j], [i + add[0], j + add[1]]] for add in [[0, 1], [1, 0], [-1, 0], [0, -1]]
                              if is_valid_move(matrix, player, [[i, j], [i + add[0], j + add[1]]], False)]
    return all_moves


class InvalidMove(Exception):
    pass


def apply_change(board, player, move):
    new_board = json.loads(json.dumps(board))
    is_valid_move(board, player, move)
    new_board[move[0][0]][move[0][1]] = EMP
    new_board[move[1][0]][move[1][1]] = player
    return new_board


class Game:
    def __init__(self, player1_type="Player", player2_type="Computer"):
        self.matrix = None
        self.turn = 0
        self.player1_type = player1_type
        self.player2_type = player2_type

    def init(self):
        self.matrix = get_default_board()
        self.turn = 0

    def start(self):
        self.init()
        print(np.matrix(np.flip(np.fliplr(self.matrix))))
        while not is_final_state(self.matrix):
            try:
                choice = self.handle_player_input()
                new_st = apply_change(self.matrix, 'O' if self.turn == 0 else 'C', choice)
            except InvalidMove as e:
                print(e)
                continue
            self.matrix = new_st
            self.turn = 1 if self.turn == 0 else 0
            print(np.matrix(np.flip(np.fliplr(self.matrix))))
        print("Game Ended. Winner: " + "1" if self.turn == 1 else "2")

    def handle_player_input(self):
        player_t = self.player1_type if self.turn == 0 else self.player2_type
        if player_t == "Player" or player_t == "Human":
            return self.handle_human_input()
        elif player_t == "Computer" or player_t == "AI":
            return self.handle_ai_input()
        raise Exception("Unknown Player Type")

    def handle_human_input(self):
        lst = None
        while True:
            try:
                lst = eval('[' + ','.join(
                    re.findall(r'[0-9]', input("Enter move player" + ("1" if self.turn == 0 else "2")))) + ']')
            finally:
                if not isinstance(lst, list) or not len(lst[0:4]) == 4:
                    print('Invalid move. Move format: 0 0 0 1. => [0, 0] to [0, 1]')
                    continue
                mv = [[lst[0], lst[1]], [lst[2], lst[3]]]
                print('moving ' + str(mv[0]) + ' to ' + str(mv[1]))
                return mv

    def handle_ai_input(self):
        lst = get_all_moves_from(self.matrix, 'C')
        values = [evaluate_1(np.flip(apply_change(self.matrix, 'C', mv))) for mv in lst]
        return lst[values.index(max(values))]


def evaluate_1(matrix):
    score = 12
    for i, row in enumerate(matrix):
        ai_pieces = [j for j, p in enumerate(row) if p == 'C']
        player_pieces = [j for j, p in enumerate(row) if p == 'O']
        score -= len(ai_pieces) * i + len(player_pieces) * i
    return score
