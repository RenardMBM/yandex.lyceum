import pygame
from __main__ import sc


class Button:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.nameOfImage = name

    def drawButton(self):
        button_surf = pygame.image.load('images/' + self.nameOfImage)
        button_rect = button_surf.get_rect(bottomright=(self.x, self.y))

        sc.blit(button_surf, button_rect)

    def drawBrightButton(self):
        brightButton_surf = pygame.image.load('images/bright_' + self.nameOfImage)
        brightButton_rect = brightButton_surf.get_rect(bottomright=(self.x, self.y))

        sc.blit(brightButton_surf, brightButton_rect)
