from game import Game
from default_strategy import DefaultStrategy
from minimax_strategy import MiniMaxStrategy

if __name__ == "__main__":
    g = Game("Player", "Computer", ai_strategy=DefaultStrategy())
    g.start()

