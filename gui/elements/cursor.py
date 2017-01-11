import pygame


class Cursor(pygame.Rect):
    def __init__(self):
        super().__init__(0, 0, 1, 1)
        self.left, self.top = pygame.mouse.get_pos()
