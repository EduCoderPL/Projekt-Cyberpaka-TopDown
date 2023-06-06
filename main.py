import random

import pygame
from pygame.locals import *

from floor import Floor
from player import Player
from wall import Wall

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.offsetX = self.offsetY = 0

        self.player = Player(100, 100, 80, 80, self)

    def main(self):
        self.init_game()
        self.game_loop()

    def init_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        ###########################
        self.wallList = []
        self.floorList = []



        ############################
        self.add_objects_to_game(5, Wall, self.wallList)
        self.add_objects_to_game(5, Floor, self.floorList)

    def game_loop(self):
        while self.running:
            self.get_input()
            self.update()
            self.check_if_close_game()
            self.draw()

        pygame.quit()

    def check_if_close_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    # Stworzenie nowej funkcji sprawdzającej, czy gracz wcisął cokolwiek na klawiaturze
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[K_d]:
            self.player.move(0.5, 0)
        if keys[K_a]:
            self.player.move(-0.5, 0)
        if keys[K_w]:
            self.player.move(0, -0.5)
        if keys[K_s]:
            self.player.move(0, 0.5)

    def update(self):
        self.player.update()
        self.offsetX = self.player.x - self.width/2
        self.offsetY = self.player.y - self.height/2
        self.solve_collisions()

    def draw(self):
        self.screen.fill(BLACK)

        for floor in self.floorList:
            floor.draw()

        for wall in self.wallList:
            wall.draw()
        self.player.draw()

        self.clock.tick(60)
        pygame.display.flip()

    def add_objects_to_game(self, count, class_name, list_for_objects):
        for i in range(count):
            rand_x = random.randint(50, self.width - 50)
            rand_y = random.randint(50, self.height - 50)

            rand_width = random.randint(100, 300)
            rand_height = random.randint(100, 300)
            new_wall = class_name(rand_x, rand_y, rand_width, rand_height, self)

            list_for_objects.append(new_wall)


    def solve_collisions(self):
        for wall in self.wallList:
            if self.player.rect.colliderect(wall.rect):
                if self.player.xVel > 0:
                    if self.player.x + self.player.width/2 > wall.x - wall.width/2:
                        self.player.x = wall.x - wall.width/2 - self.player.width/2
                        self.player.xVel = 0
                        self.player.update_rect()

                elif self.player.xVel < 0:
                    if self.player.x - self.player.width/2 < wall.x + wall.width/2:
                        self.player.x = wall.x + wall.width/2 + self.player.width/2
                        self.player.xVel = 0
                        self.player.update_rect()

                elif self.player.yVel > 0:
                    if self.player.y + self.player.height / 2 > wall.y - wall.height / 2:
                        self.player.y = wall.y - wall.height / 2 - self.player.height / 2
                        self.player.yVel = 0
                        self.player.update_rect()

                elif self.player.yVel < 0:
                    if self.player.y - self.player.height / 2 < wall.y + wall.height / 2:
                        self.player.y = wall.y + wall.height / 2 + self.player.height / 2
                        self.player.yVel = 0
                        self.player.update_rect()



game = Game(1366, 768)
game.main()
