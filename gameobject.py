import pygame
from pygame.locals import *
class GameObject:

    def __init__(self, x: int, y: int, width: int, height: int, game, image_src):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.game = game

        self.img = pygame.transform.scale(pygame.image.load(image_src), (self.width, self.height))
        self.rect = Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    def draw(self):
        self.drawX = self.x - self.game.offsetX
        self.drawY = self.y - self.game.offsetY
        self.game.screen.blit(self.img, (self.drawX - self.width / 2, self.drawY - self.height / 2))