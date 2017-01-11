from core.game.const import *
from util.vectors import find_random


class MiniMax:
    def __init__(self, game, max_deep=9):
        self.game = game
        self.max_deep = max_deep

    def predict(self):
        return self.run(get_result=True)

    def run(self, pgame=None, deep=1, get_result=False):
        game = pgame or self.game

        # Base Case
        if game.state != CONTINUE or deep == self.max_deep:
            return game.evaluate()

        possibilities = []

        for move in game.move_all():
            play = self.run(move, deep + 1)
            possibilities.append(play)

        if get_result:
            best = max(possibilities)
            moves = self.game.possibilities
            return moves[find_random(possibilities, best)]

        if game.current_player == game.original_player:
            return max(possibilities)
        else:
            return min(possibilities)
