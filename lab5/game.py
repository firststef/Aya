import json
import numpy as np
import re
from board import get_default_board, is_final_state, apply_change, InvalidMove
from default_strategy import DefaultStrategy


class GoBackMove(Exception):
    pass


class Game:
    def __init__(self, player1_type="Player", player2_type="Computer", ai_strategy=DefaultStrategy()):
        self.matrix = None
        self.turn = 0
        self.player1_type = player1_type
        self.player2_type = player2_type
        self.move_stack = []
        self.ai_strategy = ai_strategy

    def init(self):
        self.matrix = get_default_board()
        self.turn = 0
        self.move_stack.append(json.loads(json.dumps(self.matrix)))

    def start(self):
        self.init()
        print(np.matrix(np.flip(np.fliplr(self.matrix))))
        while not is_final_state(self.matrix):
            try:
                choice = self.handle_player_input()
                new_st = apply_change(self.matrix, 'O' if self.turn == 0 else 'C', choice)
                self.move_stack.append(json.loads(json.dumps(self.matrix)))
            except InvalidMove as e:
                print(e)
                continue
            except GoBackMove:
                if len(self.move_stack) >= 2:
                    self.matrix = self.move_stack.pop()
                    self.matrix = self.move_stack.pop()
                    print('Reverted')
                    print(np.matrix(np.flip(np.fliplr(self.matrix))))
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
                input_t = input("Enter move player" + ("1" if self.turn == 0 else "2"))
                if input_t == "back":
                    raise GoBackMove
                lst = eval('[' + ','.join(
                    re.findall(r'[0-9]', input_t)) + ']')
            except GoBackMove as g:
                raise g
            except InvalidMove:
                pass
            if not isinstance(lst, list) or not len(lst[0:4]) == 4:
                print('Invalid move. Move format: 0 0 0 1. => [0, 0] to [0, 1]')
                continue
            mv = [[lst[0], lst[1]], [lst[2], lst[3]]]
            print('moving ' + str(mv[0]) + ' to ' + str(mv[1]))
            return mv

    def handle_ai_input(self):
        return self.ai_strategy(self.matrix, 'O' if self.turn == 0 else 'C')
