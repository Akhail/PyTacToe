from sys import exit

from pygame import event, init, mouse
from pygame.locals import QUIT, MOUSEBUTTONDOWN

from core.game.tictactoe import TicTacToe
from core.ia.minimax import MiniMax
from core.game.const import CONTINUE
from core.utils.coord import convert_to_number
from gui.main.game import Game
from gui.main.const import *

gui, ia, game = None, None, None


def events():
    for evt in event.get():
        if evt.type == QUIT:
            exit(0)
        x, y = mouse.get_pos()
        if x <= WIDTH and evt.type == MOUSEBUTTONDOWN:
            px = x // (WIDTH / 3)
            py = y // (HEIGHT / 3)
            xy = convert_to_number(px, py)
            
            if not gui.vs_human:
                ant = gui.mode
                gui.mode = "Pensando.."
                gui.update()
                game.move(ia.predict())
                gui.mode = ant
            

def main():
    global game, ia, gui
    game = TicTacToe()
    ia = MiniMax(game)
    gui = Game(game.board)
    while True:
        events()
        gui.update()
        if game.state != CONTINUE:
            game.new_game()
    exit(0)

if __name__ == '__main__':
    init()
    main()
