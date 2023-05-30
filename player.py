import pygame

class Player:
    def __init__(self, x: int, y: int, width: int, height: int, game):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.game = game

        self.xVel = 0
        self.yVel = 0
        self.img = pygame.transform.scale(pygame.image.load("player.png"), (self.width, self.height))

    def move(self, x: float, y: float):
        self.xVel += x
        self.yVel += y

    def update(self):
        # OPÓR
        self.xVel *= 0.95
        self.yVel *= 0.95

        self.x += self.xVel
        self.y += self.yVel

    def draw(self):
        self.game.screen.blit(self.img, (self.x - self.width/2, self.y - self.height/2))
