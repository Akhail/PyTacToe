from copy import copy
import numpy as np

from core.game.const import *


class TicTacToe:
    def __init__(self, pos=None):
        if pos is None:
            self.board = np.zeros(9, int)
            self.current_player = X
        else:
            self.board = np.array(pos)
            if pos.count(X) > pos.count(O):
                self.current_player = O
            else:
                self.current_player = X
        self.original_player = self.current_player
        self.is_copy = False
        self.possibilities = None
        self.state = None
        self.calc_possibilities()
        self.calc_state()
        self.game_count = 0
        self.player_win = 0
        self.last_move = []

    def new_game(self):
        self.current_player = X
        self.original_player = self.current_player
        self.game_count += 1
        self.last_move = []

        if self.state != CONTINUE:
            self.player_win += self.state

        self.board[:] = 0
        self.calc_state()
        self.calc_possibilities()

    def print(self):
        for idx, x in enumerate(self.board):
            print('[' + Play[x] + ']', end=' ')

            if (idx+1) % 3 == 0:
                print()
                
    def calc_state(self):
        bd = self.board
        pos = 9 - np.count_nonzero(self.board)
        # Row
        if bd[0] == bd[1] == bd[2] != Non:
            self.state = bd[0]
        elif bd[3] == bd[4] == bd[5] != Non:
            self.state = bd[3]
        elif bd[6] == bd[7] == bd[8] != Non:
            self.state = bd[6]

        # Column
        elif bd[0] == bd[3] == bd[6] != Non:
            self.state = bd[0]
        elif bd[1] == bd[4] == bd[7] != Non:
            self.state = bd[1]
        elif bd[2] == bd[5] == bd[8] != Non:
            self.state = bd[2]

        # Diagonal
        elif bd[0] == bd[4] == bd[8] != Non:
            self.state = bd[0]
        elif bd[6] == bd[4] == bd[2] != Non:
            self.state = bd[6]

        elif pos == 0:
            self.state = TABLE
        else:
            self.state = CONTINUE

    def calc_possibilities(self):
        self.possibilities = np.arange(9)[self.board == Non]
        # self.possibilities = np.delete(self.possibilities, self.equiv())

    def move_all(self):
        for move in self.possibilities:
            cop = copy(self)
            cop.move(move)
            yield cop

    def move(self, move):
        if move in self.possibilities:
            self.board[move] = self.current_player
            self.current_player *= -1
            if not self.is_copy:
                self.original_player = self.current_player
            self.last_move.append(move)
            self.calc_possibilities()
            self.calc_state()
            return True

        return False

    # noinspection PyTypeChecker
    def evaluate(self):
        end = self.state

        if end == self.original_player * -1:
            return -10
        if end == self.original_player:
            return 10
        if end == TABLE:
            return 0

        tmp = self.board.copy()
        tmp[tmp == self.original_player] = 0
        eq0 = tmp.reshape(3, 3) == 0

        cant_mov = np.count_nonzero(np.all(eq0, axis=0))  # Free Columns
        cant_mov += np.count_nonzero(np.all(eq0, axis=1))  # Free Rows
        cant_mov += np.count_nonzero(np.all(tmp[::4] == 0))  # Free Diag
        cant_mov += np.count_nonzero(np.all(tmp[2:7:2] == 0))  # Free secondary diag

        tmp = self.board.copy()
        tmp[tmp == self.original_player * -1] = 0
        eq0 = tmp.reshape(3, 3) == 0

        cant_mov -= np.count_nonzero(np.all(eq0, axis=0))  # Free Columns
        cant_mov -= np.count_nonzero(np.all(eq0, axis=1))  # Free Rows
        cant_mov -= np.count_nonzero(np.all(tmp[::4] == 0))  # Free Diag
        cant_mov -= np.count_nonzero(np.all(tmp[2:7:2] == 0))  # Free Secondary Diag

        return cant_mov

    def __copy__(self):
        c = TicTacToe()
        c.last_move = self.last_move
        c.current_player = self.current_player
        c.original_player = self.original_player
        c.is_copy = True
        c.board = self.board.copy()
        return c

    # def equiv(self):
    #     sim = []
    #     equal = 0
    #     ant = -1
    #     for idx, mov in enumerate(self.possibilities[:2]):
    #         board = self.board.copy()
    #         board[mov] = 2
    #         for idx2, test in enumerate(self.possibilities[idx+1:]):
    #             temp = self.board.copy()
    #             temp[test] = 2
    #             for x in range(1, 5):
    #                 other = np.rot90(temp.reshape(3,3), x).ravel()
    #
    #                 # noinspection PyTypeChecker
    #                 if np.all(other == board):
    #                     if ant != equal:
    #                         sim.append([mov, test])
    #                         ant = equal
    #                     else:
    #                         sim[equal].append(test)
    #         if ant == equal:
    #             sim[equal].remove(np.random.choice(sim[equal]))
    #             equal += 1
    #     return sim
