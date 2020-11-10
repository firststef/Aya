from evaluate import evaluate_2
from game import Game
from alphabetapruning_strategy import AlphaBetaPruningStrategy
from default_strategy import DefaultStrategy
from minimax_strategy import MiniMaxStrategy

if __name__ == "__main__":
    g = Game("Player", "Computer", ai_strategy=AlphaBetaPruningStrategy(4, evaluate=evaluate_2))
    g.start()

