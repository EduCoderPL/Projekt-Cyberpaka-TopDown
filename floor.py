
import pygame
from pygame.locals import *

from gameobject import GameObject


class Floor(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, game):
        super().__init__(x, y, width, height, game, "images/floor.png")


