# Modules
import pygame

from core.game.const import *
from core.utils.coord import convert_to_number
from gui.elements.button import Button
from gui.main.const import *


# Class
class Game:
    def __init__(self, board):
        self.screen = pygame.display.set_mode((WIDTH + MENU_WIDTH, HEIGHT))
        pygame.display.set_caption('Tres en raya')
        self.font = pygame.font.Font(None, 100)
        self.mode = 'vs Computadora'
        self.b1 = Button(self.screen, self.change_type, 'vs Humano', width=130)
        self.b1.pos_x = WIDTH + (MENU_WIDTH / 2)
        self.b1.pos_y = HEIGHT * .229
        self.vs_human = False
        self.b2 = Button(self.screen, self.change_type, 'vs Computadora', width=160)
        self.b2.pos_x = WIDTH + (MENU_WIDTH / 2)
        self.b2.pos_y = HEIGHT * .229 + 50
        self.board = board
        self.update()
    
    def update(self):
        self.screen.fill(DARK)
        self.draw_menu()
        self.draw_board()
        
    def change_type(self, evt):
        if evt.text_str == "vs Computadora":
            self.mode = "vs Computadora"
            self.vs_human = False
        else:
            self.mode = "vs Humano"
            self.vs_human = False
        
    def draw_menu(self):
        # Se escribe 'Tres en raya' en la pantalla
        text = pygame.font.Font(None, 50).render('Tres en raya', True, RED)
        rect_text = text.get_rect()
        rect_text.centerx = WIDTH + (MENU_WIDTH / 2)
        rect_text.centery = HEIGHT * .08
        self.screen.blit(text, rect_text)
        
        self.b1.draw()
        self.b2.draw()
        
        # Muestra el modo de juego
        text = pygame.font.Font(None, 20).render(self.mode, True, BLUE)
        rect_text = text.get_rect()
        rect_text.centerx = WIDTH + (MENU_WIDTH / 2)
        rect_text.centery = HEIGHT - 30
        self.screen.blit(text, rect_text)
    
    def draw_board(self):
        # Dibuja el tablero de juego
        pygame.draw.line(self.screen, RED, (5, HEIGHT / 3), (WIDTH - 5, HEIGHT / 3))
        pygame.draw.line(self.screen, RED, (5, 2 * HEIGHT / 3), (WIDTH - 5, 2 * HEIGHT / 3))
        
        pygame.draw.line(self.screen, RED, (WIDTH / 3, 5), (WIDTH / 3, HEIGHT - 5))
        pygame.draw.line(self.screen, RED, (2 * WIDTH / 3, 5), (2 * WIDTH / 3, HEIGHT - 5))
        for y in range(3):
            for x in range(3):
                xy = convert_to_number(x, y)
                if self.board[xy] != Non:
                    mov = self.font.render(Play[self.board[xy]], 0, RED)
                    self.screen.blit(mov, (80 + x * WIDTH / 3, (y + 1) * HEIGHT / 3 - 110))
        
        pygame.display.flip()
    
    # def move(self, player, x, y):
    #     temp = self.mode
    #     self.board = next_move(self.board, player, (x, y))
    #
    #     if not self.vs_human:
    #         self.mode = "Calculando movimiento"
    #     self.update()
    #     if not self.vs_human:
    #         self.board = next_move(self.board, player * -1, minimax(self.board))
    #         self.mode = temp
    #         self.update()
