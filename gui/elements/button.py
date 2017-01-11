import pygame
from pygame.locals import MOUSEBUTTONDOWN

from gui.elements.cursor import Cursor
from gui.main.const import *


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, event, text='', colour=RED, hover=RED_LIGHT, width=50, height=30):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.surface = pygame.Surface((width, height))
        self.text_str = text
        self.text = None
        self.pos_x = 0
        self.pos_y = 0
        self.rect = self.surface.get_rect()
        self.color = colour
        self.hover = hover
        self.width = width
        self.event = event
        self.height = height
        self.change_color(self.color)
    
    def is_hover(self):
        cursor = Cursor()
        rect = self.surface.get_rect()
        rect.top = self.pos_y - self.surface.get_rect().centery
        rect.left = self.pos_x - self.surface.get_rect().centerx
        
        if cursor.colliderect(rect):
            self.change_color(self.hover, WHITE)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.event(self)
        else:
            self.change_color(self.color, WHITE)
    
    def change_color(self, background, foreground=WHITE):
        self.surface.fill(background)
        self.text = pygame.font.Font(None, 20).render(self.text_str, True, foreground)
    
    def draw(self):
        self.is_hover()
        rect_text = self.text.get_rect()
        rect_text.centerx = self.surface.get_rect().centerx
        rect_text.centery = self.surface.get_rect().centery
        self.surface.blit(self.text, rect_text)
        self.screen.blit(self.surface,
                         (self.pos_x - self.surface.get_rect().centerx, self.pos_y - self.surface.get_rect().centery))
