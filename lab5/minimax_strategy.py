from board import get_all_moves_from, apply_change
from evaluate import evaluate_1


class MiniMaxStrategy:
    def __init__(self, depth, evaluate=evaluate_1, get_all_moves=get_all_moves_from, apply_move=apply_change):
        self.depth = depth
        self.evaluate = evaluate
        self.get_all_moves = get_all_moves
        self.apply_move = apply_move

    def __call__(self, matrix, ai_player):
        return self.minimax(matrix, 0, 'C')

    def minimax(self, matrix, level, turn):
        if self.depth - level == 0:
            return None

        moves = self.get_all_moves(matrix, turn)
        if len(moves) == 0:
            return None

        new_turn = 'O' if turn == 'C' else 'C'
        minimax_val = [self.minimax(self.apply_move(matrix, turn, mv), level + 1, new_turn) for mv in moves]
        values = [
            (
                self.evaluate(self.apply_move(matrix, turn, moves[i]))
                if minimax_val[i] is None else
                minimax_val[i]
            )
            for i in range(len(moves))
        ]

        if level == 0:
            return moves[values.index(max(values))]
        else:
            return max(values) if turn == 'C' else min(values)
