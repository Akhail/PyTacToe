import os

from core.game.const import *
from core.game.tictactoe import TicTacToe
from core.ia.minimax import MiniMax
import time


def main():
    game = TicTacToe()
    game.move(4)
    ia = MiniMax(game, max_deep=9)
    while game.state == CONTINUE:
        for _ in range(2):
            if game.current_player == O:
                os.system('clear')
                game.print()
                game.move(ia.predict())
            else:
                os.system('clear')
                game.print()
                # mov = input('Mov: ')
                # xx, yy = str.split(mov, ',')
                # xx, yy = int(xx) - 1, int(yy) - 1
                # game.move(xx + yy * 3)
                game.move(ia.predict())
            time.sleep(1)


if __name__ == '__main__':
    main()
