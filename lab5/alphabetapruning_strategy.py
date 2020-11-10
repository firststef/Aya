import math

from board import get_all_moves_from, apply_change
from evaluate import evaluate_1


class AlphaBetaPruningStrategy:
    def __init__(self, depth, evaluate=evaluate_1, get_all_moves=get_all_moves_from, apply_move=apply_change):
        self.depth = depth
        self.evaluate = evaluate
        self.get_all_moves = get_all_moves
        self.apply_move = apply_move

    def __call__(self, matrix, ai_player):
        return self.minimax(matrix, 0, 'C', -math.inf, math.inf)

    def minimax(self, matrix, level, turn, alpha, beta):
        if self.depth - level == 0:
            return None

        moves = self.get_all_moves(matrix, turn)
        if len(moves) == 0:
            return None

        final_val = -math.inf if turn == 'C' else math.inf
        best_mv = None
        for mv in moves:
            minimax_ret = self.minimax(self.apply_move(matrix, turn, mv), level + 1, 'O' if turn == 'C' else 'C', alpha, beta)
            val = self.evaluate(self.apply_move(matrix, turn, mv)) if minimax_ret is None else minimax_ret
            if turn == 'C':
                if final_val < val:
                    final_val = val
                    best_mv = mv
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            else:
                if final_val > val:
                    final_val = val
                    best_mv = mv
                beta = min(beta, val)
                if alpha >= beta:
                    break

        if level == 0:
            return best_mv
        else:
            return final_val
