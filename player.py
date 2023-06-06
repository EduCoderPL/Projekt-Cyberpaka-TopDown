import pygame
from pygame.locals import Rect

from gameobject import GameObject


class Player(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, game):

        super().__init__(x, y, width, height, game, "images/player.png")
        self.xVel = 0
        self.yVel = 0

    def move(self, x: float, y: float):
        self.xVel += x
        self.yVel += y

    def update(self):
        # OPÓR
        self.xVel *= 0.95
        self.yVel *= 0.95

        self.x += self.xVel
        self.y += self.yVel

        self.rect = Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)

    def update_rect(self):
        self.rect = Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
