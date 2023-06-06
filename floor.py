
import pygame
from pygame.locals import *
class Floor:
    def __init__(self, x: int, y: int, width: int, height: int, game):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.game = game

        self.img = pygame.transform.scale(pygame.image.load("wall.png"), (self.width, self.height))

    def draw(self):
        self.game.screen.blit(self.img, (self.x - self.width/2, self.y - self.height/2))