from nose.tools import assert_equal
from core.game.tictactoe import TicTacToe
from core.ia.minimax import MiniMax
from core.game.const import *
import numpy as np


class TestMinMax:
    # noinspection PyAttributeOutsideInit
    def setup(self):
        self.game = TicTacToe()
        self.ia = MiniMax(self.game)
    
    def test_predict_ia_ia(self):
        self.game.move(0)
        while self.game.state == CONTINUE:
            self.game.move(self.ia.predict())
        assert_equal(self.game.state, TABLE)

    def test_predict_ia_human(self):
        self.game.move(0)
        self.game.move(4)
        self.game.move(1)
        assert_equal(self.ia.predict(), 2)
        self.game.move(2)
        self.game.move(3)
        assert_equal(self.ia.predict(), 6)