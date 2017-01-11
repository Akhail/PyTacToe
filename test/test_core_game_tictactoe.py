import numpy as np
from core.game.tictactoe import TicTacToe
from core.game.const import *


class TestTicTacToe:
    # noinspection PyAttributeOutsideInit
    def setup(self):
        self.game = TicTacToe()

    # noinspection PyTypeChecker
    def test_move(self):
        bd = self.game.board
        assert np.all(bd == 0)
        
        moved = self.game.move(0)
        assert moved
        assert bd[0] == X

    def test_calc_state(self):
        self.game.board = np.array([X, O, X, X, O, X, O, X, O])
        self.game.calc_state()
        assert self.game.state == TABLE

        self.game.board = np.array([X, O, X, O, X, O, 0, 0, 0])
        self.game.calc_state()
        assert self.game.state == CONTINUE

        self.game.board = np.array([O, O, O, X, X, 0, X, 0, 0])
        self.game.calc_state()
        assert self.game.state == WIN_PLAYER_2
        
        self.game.board = np.array([X, O, X, O, X, O, X, 0, 0])
        self.game.calc_state()
        assert self.game.state == WIN_PLAYER_1
